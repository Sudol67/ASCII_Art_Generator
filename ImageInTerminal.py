import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
from PIL import Image

def image_manipulation(image):
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #change to greyscale

    twoDimage = grey_image.reshape((-1, 1))
    twoDimage = np.float32(twoDimage)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    attempts = 10

    ret, label, center = cv.kmeans(twoDimage, K, None, criteria, attempts, cv.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape(grey_image.shape)
    return result_image, K

def image_show(final_image):
    input_image_rgb = cv.cvtColor(final_image, cv.COLOR_BGR2RGB)
    plt.imshow(input_image_rgb)
    plt.axis('off')
    plt.title("Image after postprocesing")
    plt.show()

def imageTerminalShow(segmented_image, K):
    #pixel_matrix = np.array(segmented_image)
    char_matrix = np.where(segmented_image > 125, "W", "█")
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    print("\n".join("".join(row) for row in char_matrix))

#fileDialog
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Choose your image",
    initialdir=documents_folder,
    filetypes=[
        ("Obrazy", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp"),
    ]
)
file_path = os.path.normpath(file_path)

if file_path:
    print(f"Wybrano plik: {file_path}")

    file_path = Path(file_path)
    input_image = cv.imread(str(file_path))

    if input_image is None:
        print("\033[31mOpenCV nie może otworzyc obrazu. Spróbuje uzyć PIL...\033[0m")
        try:
            pil_image = Image.open(file_path)
            input_image = np.array(pil_image)
            input_image = cv.cvtColor(input_image, cv.COLOR_RGB2BGR)
            print("\033[32mSukces: obraz załadowany przez PIL\033[0m")
        except Exception as e:
            print(f"\033[31mBłąd podczas ładowania obrazu przez PIL: {e}\033[0m")
            input_image = None
    
    height, width = input_image.shape[:2]
    print("Rozmiar wczytango zdjecia:")
    print(f"Szerokosc: {width} px")
    print(f"Wysokosc: {height} px")

    if width > 200 or height > 200:
        max_size = 100
        scale = max_size / max(height, width)
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_image = cv.resize(input_image, (new_width, new_height), interpolation=cv.INTER_AREA)

        heightChanged, widthChanged = resized_image.shape[:2]
        print("\nNowe wymiary zdjęcia:")
        print(f"Szerokosc: {heightChanged} px")
        print(f"Wysokosc: {widthChanged} px")

        segmented_image, K = image_manipulation(resized_image)
    else:
        segmented_image, K = image_manipulation(input_image)
    
    imageTerminalShow(segmented_image, K)

else:
    print("Nie wybrano pliku.")


#próbowanie różnych znaków do wyświetlania, problem wyrównania outputu, jakie znaki użyć, zacząć od małej ilości znaków