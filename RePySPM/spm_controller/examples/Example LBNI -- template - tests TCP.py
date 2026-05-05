# import sys
# import os

# import socket

# def main():

#     HOST = "127.0.0.1"   # IP onde está LabVIEW
#     PORT = 6340          # porto onde LabVIEW está escoitando


#     def send_command(sock, command):
#         payload = (command + "\r\n").encode("ascii")
#         sock.sendall(payload)

#         response = sock.recv(1024)
#         return response.decode("ascii", errors="replace").strip()

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.settimeout(5)
#         s.connect((HOST, PORT))

#         print("Conectado a LabVIEW")

#         while True:
#             command = input("cmd> ")

#             if command.lower() in ("quit", "exit", "q"):
#                 send_command(s, "quit")
#                 break

#             try:
#                 reply = send_command(s, command.lower())
#                 print("LabVIEW:", reply)
#             except UnicodeEncodeError:
#                 print("Erro: usa só ASCII.")
#             except socket.timeout:
#                 print("Timeout esperando resposta de LabVIEW.")
#             except OSError as e:
#                 print("Erro de conexión:", e)
#                 break

# print("Conexión pechada.")
    
# if __name__ == "__main__":
#     main()


import socket
import struct
import json
import numpy as np


HOST = "127.0.0.1"
PORT = 6340


def recv_exact(sock, nbytes):
    chunks = []
    received = 0

    while received < nbytes:
        chunk = sock.recv(nbytes - received)
        if not chunk:
            raise ConnectionError("Conexión pechada antes de recibir todos os datos")
        chunks.append(chunk)
        received += len(chunk)

    return b"".join(chunks)


def recv_message(sock):
    # 1) Ler lonxitude da cabeceira JSON
    raw_header_len = recv_exact(sock, 4)
    header_len = struct.unpack(">I", raw_header_len)[0]

    # 2) Ler cabeceira JSON
    raw_header = recv_exact(sock, header_len)
    header = json.loads(raw_header.decode("utf-8"))

    # 3) Ler payload
    nbytes = int(header.get("nbytes", 0))
    payload = recv_exact(sock, nbytes) if nbytes > 0 else b""

    # 4) Decodificar segundo tipo
    value = decode_payload(header, payload)

    return header, value


def decode_payload(header, payload):
    typ = header["type"]

    if typ == "string":
        encoding = header.get("encoding", "utf-8")
        return payload.decode(encoding)

    if typ == "bool":
        if len(payload) != 1:
            raise ValueError("Un boolean debería ter exactamente 1 byte")
        return payload[0] != 0

    if typ == "number":
        dtype = numpy_dtype(header)
        arr = np.frombuffer(payload, dtype=dtype)
        if arr.size != 1:
            raise ValueError("Un number debería conter exactamente un valor")
        return arr.astype(dtype.newbyteorder("="))[0]

    if typ == "array":
        dtype_name = header["dtype"]
        shape = tuple(header["shape"])

        if dtype_name == "bool":
            arr = np.frombuffer(payload, dtype=np.uint8)
            arr = arr.astype(bool)
        else:
            dtype = numpy_dtype(header)
            arr = np.frombuffer(payload, dtype=dtype)
            arr = arr.astype(dtype.newbyteorder("="))

        expected_items = int(np.prod(shape))
        if arr.size != expected_items:
            raise ValueError(
                f"Tamaño incorrecto: recibín {arr.size} elementos, "
                f"pero esperaba {expected_items} para shape={shape}"
            )

        return arr.reshape(shape)

    if typ == "empty":
        return None

    raise ValueError(f"Tipo non soportado: {typ!r}")


def numpy_dtype(header):
    dtype_name = header["dtype"]
    endian = header.get("endian", "big")

    if endian == "big":
        prefix = ">"
    elif endian == "little":
        prefix = "<"
    elif endian == "native":
        prefix = "="
    else:
        raise ValueError(f"Endian inválido: {endian!r}")

    return np.dtype(prefix + dtype_name)


def send_command(sock, command):
    payload = (command + "\r\n").encode("ascii")
    sock.sendall(payload)
    return recv_message(sock)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((HOST, PORT))

        print("Conectado a LabVIEW")

        while True:
            command = input("cmd> ").strip()

            if command.lower() in ("quit", "exit", "q"):
                send_command(s, "close")
                break

            try:
                header, value = send_command(s, command)

                print("Header:", header)
                print("Value:")
                print(value)

                if isinstance(value, np.ndarray):
                    print("Shape:", value.shape)
                    print("Dtype:", value.dtype)

            except socket.timeout:
                print("Timeout esperando resposta de LabVIEW.")
            except Exception as e:
                print("Erro:", e)

    print("Conexión pechada.")


if __name__ == "__main__":
    main()