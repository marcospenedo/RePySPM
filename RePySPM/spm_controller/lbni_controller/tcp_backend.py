import socket
import struct
import json
import numpy as np


class TCPBackend:
    """TCP backend for AFMController. Communicates with LabVIEW via JSON+payload protocol."""

    def __init__(self, host, port=6340):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        print(f"Connecting to LabVIEW via TCP: {self.host}:{self.port}")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(10)
        self.sock.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")

    def disconnect(self):
        print(f"Disconnecting from {self.host}:{self.port}")
        if self.sock:
            try:
                self._send_raw("close")
                self._recv_message()  # LabVIEW responds with OK on close
            except Exception:
                pass
            self.sock.close()
            self.sock = None

    _ERROR_RESPONSE = "Indicator/control not found"

    def write_control(self, command):
        self._send_raw(command)
        _, value = self._recv_message()
        if isinstance(value, str) and value == self._ERROR_RESPONSE:
            raise RuntimeError(f"LabVIEW error for command '{command}': {value}")
        return 0

    def read_control(self, command, control_name):
        self._send_raw(command)
        _, value = self._recv_message()
        if isinstance(value, str) and value == self._ERROR_RESPONSE:
            raise RuntimeError(f"LabVIEW error for command '{command}': {value}")
        return value

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _send_raw(self, command):
        payload = (command + "\r\n").encode("ascii")
        self.sock.sendall(payload)

    def _recv_exact(self, nbytes):
        chunks = []
        received = 0
        while received < nbytes:
            chunk = self.sock.recv(nbytes - received)
            if not chunk:
                raise ConnectionError("Connection closed before all data was received")
            chunks.append(chunk)
            received += len(chunk)
        return b"".join(chunks)

    def _recv_message(self):
        raw_header_len = self._recv_exact(4)
        header_len = struct.unpack(">I", raw_header_len)[0]

        raw_header = self._recv_exact(header_len)
        header = json.loads(raw_header.decode("utf-8"))

        nbytes = int(header.get("nbytes", 0))
        payload = self._recv_exact(nbytes) if nbytes > 0 else b""

        value = self._decode_payload(header, payload)
        return header, value

    def _decode_payload(self, header, payload):
        typ = header["type"]

        if typ == "string":
            encoding = header.get("encoding", "utf-8")
            return payload.decode(encoding)

        if typ == "string_array":
            encoding = header.get("encoding", "utf-8")
            return json.loads(payload.decode(encoding))

        if typ == "bool":
            if len(payload) != 1:
                raise ValueError("A bool payload must be exactly 1 byte")
            return payload[0] != 0

        if typ == "number":
            dtype = self._numpy_dtype(header)
            arr = np.frombuffer(payload, dtype=dtype)
            if arr.size != 1:
                raise ValueError("A number payload must contain exactly one value")
            return arr.astype(dtype.newbyteorder("="))[0]

        if typ == "array":
            dtype_name = header["dtype"]
            shape = tuple(header["shape"])
            if dtype_name == "bool":
                arr = np.frombuffer(payload, dtype=np.uint8).astype(bool)
            else:
                dtype = self._numpy_dtype(header)
                arr = np.frombuffer(payload, dtype=dtype).astype(dtype.newbyteorder("="))
            expected = int(np.prod(shape))
            if arr.size != expected:
                raise ValueError(
                    f"Size mismatch: received {arr.size} elements, "
                    f"expected {expected} for shape={shape}"
                )
            return arr.reshape(shape)

        if typ == "empty":
            return None

        raise ValueError(f"Unsupported type: {typ!r}")

    def _numpy_dtype(self, header):
        dtype_name = header["dtype"]
        endian = header.get("endian", "big")
        prefix = {"big": ">", "little": "<", "native": "="}.get(endian)
        if prefix is None:
            raise ValueError(f"Invalid endian: {endian!r}")
        return np.dtype(prefix + dtype_name)
