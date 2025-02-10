# Convert image to ASCII art

This app was created purely for private use and out of curiosity. I had a desire to experiment with openCV library. This is one of the few apps created while experimenting with this image manipulation library.

Basic functionality:
* App is mostly controlled with inputs via terminal
* After compiling, a menu with all the options shows up
* User is required to enter desired option. Note that some options are locked until user performes previous steps
* The steps are numbered on the menu
* Enter 'X' or 'x' to close the app

Menu:
1. Loading chosen image. This section performes basic path and file read. This part uses tkinter and window for user convinence. PIL library has been used in this part due to special for my country letters not supported by basic path reading.
2. Cropping image - Due to terminal having limited character space, loeaded image needs to be scaled. Program checks if the image exceeds 200px limit and if so, scaling is performed. At this point width compensation is also performed. Due to characters being on average two times higher than their width, Image needs to be streched to maintain proportions.
3. Segmentation - This part performs image manipulation. It creates B&W version of the input image. Then image segmentation is performed. Segmentation is based on the article by Gaurav Maindola from [this site](https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/). The copy of the article is saved as .pdf file in this repository.
4. Terminal print - Printing to ASCII output starts with creating matrix. Every cell of matrix corresponds to one pixel of the picture. Due to the picture being B&W it has only one channel. Program reads this channel and it's value ranging from 1 to 255. Than Every value is replaced with ASCII character from string. It is performed by dividing range 1-255 to sections. the number of sections is determined by amount of ASCII signs in string. It should be the same number as 'K'. At the end it is printed to terminal.
5. matplotlibr print - This option is used for displaying input image. It works at every point showing how image looks 'right now'. 

Technologies used:
* Python (required version 3.10 or higher)
* OpenCV
* matplotlib
* tkinter
* numpy
* PIL
