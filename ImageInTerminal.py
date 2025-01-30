import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk 
from tkinter import filedialog
import os

def image_manipulation(image):
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #change to greyscale
    return final_image

def image_show(final_image):
    input_image_rgb = cv.cvtColor(final_image, cv.COLOR_BGR2RGB)
    plt.imshow(input_image_rgb)
    plt.axis('off')
    plt.title("Image after postprocesing")
    plt.show()

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

if file_path:
    input_image = cv.imread(file_path)
    final_image = image_manipulation(input_image)
    image_show(final_image)    
else:
    print("Nie wybrano pliku.")


#pytanie użytkownika o wielkość obrazu z limitem
#Wczytywanie, kolor szarości, resize w zależności od wielkości czyli obliczenie jak mocno zmniejszyć
#segmentacja, próbowanie różnych znaków do wyświetlania, problem wyrównania outputu, jakie znaki użyć, zacząć od małej ilości znaków