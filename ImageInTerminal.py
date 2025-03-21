#Required Python 3.10 or newer
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
from PIL import Image

isLoaded = False
isCropped = False
isSegmented = False

def imageLoad():
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

    root = tk.Tk()
    root.attributes("-topmost", True)  # Force window to stay on top
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
        print(f"\033[32mChosen file: {file_path}\033[0m")

        file_path = Path(file_path)
        input_image = cv.imread(str(file_path))

        if input_image is None:
            print("\033[31mOpenCV is not able to open file. Trying to load using PIL...\033[0m")
            try:
                pil_image = Image.open(file_path)
                input_image = np.array(pil_image)
                input_image = cv.cvtColor(input_image, cv.COLOR_RGB2BGR)
                print("\033[32mSucces: image has been loaded using PIL\033[0m")
            except Exception as e:
                print(f"\033[31mError while loading image with PIL: {e}\033[0m")
                input_image = None
        
        height, width = input_image.shape[:2]
        print("\033[34mSize of the image:\033[0m")
        print(f"- Width: {width} px")
        print(f"- Height: {height} px")

        return input_image
    else:
        print("Choosing file has been suspended.")
        return

def changeSize(input_photo):
    if input_photo is None:
        print(f"\033[31mNo photo has been loaded. Use option '1' from menu.\033[0m")
        return

    height, width = input_photo.shape[:2]
    if width > 200 or height > 200:
        max_size = 100
        aspect_ratio = 2
        scale = max_size / max(height, width)
        new_width = int(width * scale * aspect_ratio)        
        new_height = int(height * scale)
        resized_image = cv.resize(input_photo, (new_width, new_height), interpolation=cv.INTER_AREA)

        heightChanged, widthChanged = resized_image.shape[:2]
        print("\033[34mNew image size:\033[0m")
        print(f"- Width: {heightChanged} px")
        print(f"- Height: {widthChanged} px")

        return resized_image
    else:
        print("No need for size correction, leaving default values")
        return input_image


def image_manipulation(image):
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #change to greyscale

    alpha = 1.5  # (>1 higher contrast, <1 lower)
    beta = 0
    contrast_image = cv.convertScaleAbs(grey_image, alpha=alpha, beta=beta)

    twoDimage = contrast_image.reshape((-1, 1))
    twoDimage = np.float32(twoDimage)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 6
    attempts = 8

    ret, label, center = cv.kmeans(twoDimage, K, None, criteria, attempts, cv.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape(grey_image.shape)
    return result_image

def image_show(final_image):
    input_image_rgb = cv.cvtColor(final_image, cv.COLOR_BGR2RGB)
    plt.imshow(input_image_rgb)
    plt.axis('off')
    plt.title("Image after postprocesing")
    plt.show()

def imageTerminalShow(segmented_image):
    ascii_chars = " .-=:+*#%@"
    char_matrix = np.array([[ascii_chars[pixel * (len(ascii_chars) - 1) // 255] for pixel in row] for row in segmented_image])
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    print("\n".join("".join(row) for row in char_matrix))

# ---------------------------------------------------------------------------------------------------------------------------------
print("\033[34mWelcome to ShellPhoto app\033[0m")

input_image = None
cropped_image = None
number = ""
currentPhoto = None
flag = 1
while flag == 1:
    print("\nChoose number from the menu below and confirm with Enter:\n1.Load photo\n2.Change photo size\n3.Photo correction\n4.Shell print\n5.Show current loaded photo state\nX.Close app")
    number = str(input("Your choice: "))

    match number:
        case '1':
            isLoaded = False
            isCropped = False
            isSegmented = False
            os.system('cls')
            print("\033[32mOpening new window, please wait...\033[0m")
            input_image = imageLoad()
            currentPhoto = input_image
            isLoaded = True
        case '2':
            os.system('cls')
            if isLoaded == True and isCropped == False and isSegmented == False:
                cropped_image = changeSize(currentPhoto)
                currentPhoto = cropped_image
                isCropped = True
            else:
                if isLoaded == False:
                    print(f"\033[31mImage is not loaded.\033[0m")
                elif isCropped:
                    print(f"\033[31mImage is already cropped.\033[0m")
                elif isSegmented:
                    print(f"\033[31mImage is already segmented, can't cropp it.\033[0m")
        case '3':
            os.system('cls')
            print("\033[32mImage has been prepared for the next step.\033[0m")
            segmentedImage = image_manipulation(currentPhoto)
            currentPhoto = segmentedImage
        case '4':
            os.system('cls')
            imageTerminalShow(currentPhoto)
        case '5':
            os.system('cls')
            image_show(currentPhoto)
        case 'X' | 'x':
            os.system('cls')
            print(f"\033[31mSee you soon...\nClosing program...\033[0m")
            exit(0)
        case _:
            print(f"\033[31mError, selected option is not recognised. Try again...\033[0m")


# Poprawić zabezpieczenia, poprawić wybór obrazu
# Poprawić kontrast by obraz był bardziej widoczny, poprawić znaki ASCII
# Poprawienie tego aby można było modyfikować rozmiar obrazu w trakcie działania bez ponownego wczytania

# Dodać obsługę filmików, może gifów