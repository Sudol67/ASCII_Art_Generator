# Convert image to ASCII shell print

This app was created purely for private use and out of curiosity. I had a desire to experiment with openCV library. This is one of the few apps created while experimenting with this image manipulation library.

Basic functionality:
* App is mostly controlled with inputs via shell
* After compiling, a menu with all the options shows up
* User is required to enter desired option. Note that some options are locked until user performes previous steps
* The steps are numbered on the menu
* Enter 'X' or 'x' to close the app

Menu:
1. Loading chosen image. This section performes basic path and file read. This part uses system file dialog for user convinence. PIL library has been used in this part due to special for my country letters not supported by basic path reading.
2. Cropping image - Due to shell having limited character space, loeaded image needs to be scaled. Program checks if the image exceeds 200px limit and if so, scaling is performed. At this point width compensation is also performed. Due to characters being on average two times higher than their width, Image needs to be streched.
3. Segmentation
4. Shell print
5. matplotlibr print


Technologies used:
* Python (required version 3.10 or higher)
* OpenCV
* matplotlib
* tkinter
* numpy
* PIL
