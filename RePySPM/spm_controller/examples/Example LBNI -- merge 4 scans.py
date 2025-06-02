import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from skimage.registration import phase_cross_correlation
from scipy.ndimage import shift

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lbni_controller import AFMController

def merge_images(images):
    """
    Fai mosaico das imaxes aliñadas baseándose en desprazamentos reais.
    Retorna a imaxe fusionada.
    """
    from skimage.registration import phase_cross_correlation
    from scipy.ndimage import shift

    ref = images[0]
    h, w = ref.shape

    # Estimamos desprazamentos con respecto á referencia
    shifts = [(0, 0)]  # ref no centro
    for img in images[1:]:
        shift_est, _, _ = phase_cross_correlation(ref, img, upsample_factor=10)
        shifts.append(shift_est)

    # Estimamos tamaño do mosaico final
    shifts = np.array(shifts)
    min_y, min_x = np.floor(np.min(shifts, axis=0)).astype(int)
    max_y, max_x = np.ceil(np.max(shifts, axis=0)).astype(int)

    # Calculamos o tamaño do canvas asegurándonos de que todas as imaxes encajen
    canvas_height = int(h + abs(min_y) + max_y)
    canvas_width = int(w + abs(min_x) + max_x)

    merged = np.zeros((canvas_height, canvas_width))
    count = np.zeros_like(merged)  # para facer media se solapa

    # Colocamos as imaxes no canvas
    for img, (dy, dx) in zip(images, shifts):
        shifted_img = shift(img, shift=(-dy, -dx))  # Shift cara ao canvas
        y_off = int(abs(min_y) - dy)
        x_off = int(abs(min_x) - dx)

        # Actualizamos as coordenadas asegurándonos de que encaixen no canvas
        y1, y2 = y_off, y_off + h
        x1, x2 = x_off, x_off + w

        # Verificamos se hai desbordamentos e axustamos se é necesario
        y1, y2 = max(0, y1), min(canvas_height, y2)
        x1, x2 = max(0, x1), min(canvas_width, x2)

        merged[y1:y2, x1:x2] += shifted_img[:y2-y1, :x2-x1]
        count[y1:y2, x1:x2] += 1

    # Evitamos división por cero
    count[count == 0] = 1
    final = merged / count

    return final



def plane_correction(image):
    """
    Substrae un plano (tilt de orde 1) da imaxe.
    """
    ny, nx = image.shape
    X, Y = np.meshgrid(np.arange(nx), np.arange(ny))
    
    # Flatten everything
    X_flat = X.ravel()
    Y_flat = Y.ravel()
    Z_flat = image.ravel()

    # Matrix para axuste do plano Z = aX + bY + c
    A = np.c_[X_flat, Y_flat, np.ones_like(X_flat)]
    coeffs, _, _, _ = np.linalg.lstsq(A, Z_flat, rcond=None)
    plane = (coeffs[0] * X + coeffs[1] * Y + coeffs[2])

    # Substrae o plano
    corrected = image - plane
    return corrected

def main():
    # Path to the project
    project_path = r"D:\\software\\Marcos\\OpenSPM-source\\"
    afm = AFMController(project_path)
    
    afm.scan_control.scan_stop()
    afm.scan_control.scan_continuous(False)
    afm.z_control.set_feedback(True)

    # Scan parameters
    scan_size = 3e-6  # 3 µm
    scan_speed = 5
    base_offset_x = 0
    base_offset_y = 0

    # Offsets para as 4 imaxes (en µm convertidas a metros)
    offsets = [
        (+1e-6, +1e-6),
        (-1e-6, +1e-6),
        (+1e-6, -1e-6),
        (-1e-6, -1e-6)
    ]

    images = []

    for i, (dx, dy) in enumerate(offsets):
        print(f"\n--- Scan {i+1} ---")

        # Set scan parameters
        afm.scan_parameters.set_width(scan_size)
        afm.scan_parameters.set_offset_x(base_offset_x + dx)
        afm.scan_parameters.set_offset_y(base_offset_y + dy)
        afm.scan_parameters.set_scan_speed(scan_speed)

        # Start scan
        afm.scan_control.scan_down()
        
        # To avoid some creep
        time.sleep(2)
        afm.scan_control.scan_down()

        # Wait until scan finishes
        while afm.scan_control.is_scanning():
            time.sleep(0.1)

        print(f"Scan {i+1} complete.")

        # Get current height image
        current_image = afm.image.get_channel("Height", 0)

        # Plane correction
        corrected_image = plane_correction(current_image)

        images.append(corrected_image)

    afm.disconnect()
    print("\n--- AFM disconnected ---")

    # --- Merge Images ---

    print("\n--- Merging Images ---")
    ref_image = images[0]
    merged = np.copy(ref_image)

    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    axs[0].imshow(ref_image, cmap='viridis')
    axs[0].set_title("Ref (0,0)")

    for i, img in enumerate(images[1:], start=1):
        shift_estimation, _, _ = phase_cross_correlation(ref_image, img, upsample_factor=10)
        shifted_img = shift(img, shift_estimation)
        merged = np.maximum(merged, shifted_img)
        axs[i].imshow(shifted_img, cmap='viridis')
        axs[i].set_title(f"Aligned {i}")

    print("\n--- Merging Images ---")
    final_merged = merge_images(images)

    plt.figure(figsize=(8, 8))
    plt.imshow(final_merged, cmap='viridis')
    plt.title("Merged Mosaic (Plane-corrected)")
    plt.colorbar(label="Height (a.u.)")
    plt.show()

if __name__ == "__main__":
    main()
