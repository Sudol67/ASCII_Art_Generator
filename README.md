# Convert image to ASCII art

This app was created purely for private use and out of curiosity. I had a desire to experiment with openCV library. This is one of the few apps created while experimenting with this image manipulation library.

### Basic functionality:
* App is mostly controlled with inputs via terminal
* After compiling, a menu with all the options shows up
* User is required to enter desired option. Note that some options are locked until user performes previous steps
* The steps are numbered on the menu
* Enter 'X' or 'x' to close the app

### Menu:
1. Loading chosen image. This section performes basic path and file read. This part uses tkinter and window for user convinence. PIL library has been used in this part due to special for my country letters not supported by basic path reading.
2. Cropping image - Due to terminal having limited character space, loeaded image needs to be scaled. Program checks if the image exceeds 200px limit and if so, scaling is performed. At this point width compensation is also performed. Due to characters being on average two times higher than their width, Image needs to be streched to maintain proportions.
3. Segmentation - This part performs image manipulation. It creates B&W version of the input image. Then image segmentation is performed. Segmentation is based on the article by Gaurav Maindola from [this site](https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/). The copy of the article is saved as .pdf file in this repository.
4. Terminal print - Printing to ASCII output starts with creating matrix. Every cell of matrix corresponds to one pixel of the picture. Due to the picture being B&W it has only one channel. Program reads this channel and it's value ranging from 1 to 255. Than Every value is replaced with ASCII character from string. It is performed by dividing range 1-255 to sections. the number of sections is determined by amount of ASCII signs in string. It should be the same number as 'K'. At the end it is printed to terminal.
5. matplotlib print - This option is used for displaying input image. It works at every point showing how image looks 'right now'. 

### Technologies used:
* Python (required version 3.10 or higher)
* OpenCV
* matplotlib
* tkinter
* numpy
* PIL

# Konwersja obrazu na grafikę ASCII

Ta aplikacja została stworzona wyłącznie do użytku prywatnego oraz z ciekawości. Chciałem poeksperymentować z biblioteką openCV. Jest to jedna z kilku aplikacji stworzonych podczas eksperymentowania z tą biblioteką.

### Podstawowa funkcjonalność:
* Aplikacja jest głównie kontrolowana za pomocą inputów w terminalu
* Po skompilowaniu pojawia się menu ze wszystkimi opcjami
* Użytkownik musi wprowadzić żądaną opcję. Należy pamiętać, że niektóre opcje są zablokowane, dopóki użytkownik nie wykona poprzednich kroków
* Kroki są ponumerowane w menu
* Aby zamknąć aplikację, należy wpisać „X” lub „x”.

### Menu:
1. Załadowanie wybranego obrazu. Ta sekcja wykonuje podstawowy odczyt ścieżki i wczytanie pliku. Ta część używa biblioteki tkinter i okna systemu dla wygody użytkownika. Biblioteka PIL została użyta w tej części ze względu na znaki specjalne nieobsługiwane przez podstawowy odczyt ścieżki.
2. Kadrowanie obrazu - Ze względu na to, że terminal ma ograniczoną ilość znaków, odczytany obraz musi zostać przeskalowany. Program sprawdza, czy obraz przekracza limit 200px, a jeśli tak, wykonywane jest skalowanie. W tym momencie wykonywana jest również kompensacja szerokości. Ponieważ znaki są średnio dwa razy wyższe niż szerokie, obraz musi zostać rozciągnięty, aby zachować proporcje.
3. Segmentacja - ta część wykonuje manipulację obrazem. Tworzy czarno-białą wersję obrazu wejściowego. Następnie wykonywana jest segmentacja obrazu. Segmentacja jest oparta na artykule Gaurava Maindoli z [tej strony] (https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/). Kopia artykułu jest zapisana jako plik .pdf w tym repozytorium.
4. Drukowanie z terminala - Drukowanie na wyjście ASCII rozpoczyna się od utworzenia macierzy. Każda komórka matrycy odpowiada jednemu pikselowi obrazu. Ponieważ obraz jest czarno-biały, ma tylko jeden kanał. Program odczytuje ten kanał i jego wartość w zakresie od 1 do 255. Następnie każda wartość jest zastępowana znakiem ASCII z ciągu znaków. Odbywa się to poprzez podzielenie zakresu 1-255 na sekcje. Liczba sekcji jest określona przez ilość znaków ASCII w zmiennej. Liczba ta powinna być taka sama liczba jak 'K'. Na koniec obraz jest wyświetlany w terminalu.
5. Wyświwtlanie normalnego obrazu - Ta opcja służy do wyświetlania obrazu wejściowego. Działa w każdym punkcie korzystania z programu, pokazując jak obraz wygląda „w tej chwili”. Wykorzystuje bibliotekę matplotlib.

### Wykorzystane technologie:
* Python (wymagana wersja 3.10 lub wyższa)
* OpenCV
* matplotlib
* tkinter
* numpy
* PIL
