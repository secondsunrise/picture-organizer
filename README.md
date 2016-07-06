# picture-organizer

***picture-organizer*** is a quick-n-dirty script I came up with to easily rename and copy picture files from one directory to another. It reads picture file names formatted in a specific way and determines which ones it can group together into a folder based on the date each was taken. ***picture-organizer*** uses `tkFileDialog` as an easy GUI for the user to select the source and target directories. Or create a target directory if one does not yet exist. 

## Requirements
* Python 2.7+
* [os](http://www.pythonforbeginners.com/os/pythons-os-module), [shutil](https://docs.python.org/2/library/shutil.html), [tkFileDialog](http://tkinter.unpythonic.net/wiki/tkFileDialog)

#### Example of tkFileDialog window

![alt text](https://cloud.githubusercontent.com/assets/17801234/16591181/e97cf5b4-4297-11e6-9e80-5124691ae06f.PNG "tkFileDialog Window")

For example, lets say you have a couple hundred pictures in this directory `C:\Users\<username>\Downloads\Pictures From 2015` all named something like `DateTaken_TimeTaken.jpg`. For example:
```
20150902_183347.jpg
20150902_183616.jpg
20150903_092934.jpg
20150908_072223.jpg
20150908_102840.jpg
20150908_102950.jpg
etc...
```

***picture-organizer*** will to sort through all of the pictures and find unique dates and then group the pictures based on the date they were taken. So the six `.jpg` files listed above would be grouped together in separate folders like so:

| 2015-09-02 | 2015-09-03 | 2015-09-08 |
|:---:|:---:|:---:|
| 20150902_183347.jpg | 20150903_092934.jpg | 20150908_072223.jpg |
| 20150902_183616.jpg | | 20150908_102840.jpg |
| | | 20150908_102950.jpg |

***picture-organizer*** will then ask for a string of text that will be appened to each folder name. Let's say I want to append the text `Family Pictures - Bobs Cell Phone` to each folder name. The folders would be named like this:
* 2015-09-02 Family Pictures - Bobs Cell Phone
* 2015-09-03 Family Pictures - Bobs Cell Phone
* 2015-09-08 Family Pictures - Bobs Cell Phone

## Flow Chart
This flow chart helps illustrate each step the program takes in chronological order when it is initiated.

1. Prompt user for the source directory
2. Prompt user for the target directory
3. Prompt user to enter the text they wish to append to each folder name
4. Create target directory (backend)
5. Create folders within the target directory (backend)
6. Copy the pictures from the source directory to their specific folders in the target directory (backend)
7. Prompt to run the program again or quit

#### Here is one full run of the script

![alt text](https://cloud.githubusercontent.com/assets/17801234/16480062/58fa8d42-3e61-11e6-98ac-455080015175.PNG "Full Run")

#### What the newly created folders look like after running the program

![alt text](https://cloud.githubusercontent.com/assets/17801234/16480108/950b9cc2-3e61-11e6-880d-95c643afcf78.PNG "Newly Created Folders")

## Futuristic Ideas
* Make it possible to use ***picture-organizer*** with files *not* formatted like `DateTaken_TimeTaken.jpg`, instead use the "Date" attribute of the file to determine which files should be grouped together.
![alt text](https://cloud.githubusercontent.com/assets/17801234/16497780/eb19e1ba-3eb5-11e6-873f-46d052ff1191.PNG "Future Date Taken Attribute")
* Add a menu allowing the user to select which part of the process they would like to complete. This would allow for more flexibility and would also enable a user to make changes if they entered incorrect information.
![alt text](https://cloud.githubusercontent.com/assets/17801234/16498104/6b96a5fc-3eb7-11e6-9086-809fcfa602f5.jpg "Future Menu System")
