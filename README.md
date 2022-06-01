# Easy-VoiceOver
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use](#how-to-use)

## General Info
This is an old project that I recently updated and reuploaded to Github. The project is a python application that is used to automize the process of creating a Voice Over video which can be used as a background for narrating a news story, a presentation, etc.
	
## Technologies
Project is created with:
* Python: 3.8
* Moviepy: 1.0.3
* google_images_download: 2.8.0 (https://github.com/Joeclinton1/google-images-download)
	
## Setup
To run this project, install requirements.txt and then just run the main.py file. Make sure Git is installed on your computer and added to PATH.

```
$ cd ../Easy-VoiceOver
$ pip install -r requirements.txt
$ python main.py
```

## How to Use
### Selecting your topic and number of images
* Enter your topic of interest and the number of images you want to DOWNLOAD.
* The program will automatically create a folder called ```downloads/``` and download the images.

![Starting the game](https://i.imgur.com/v91OK1u.png?1)


### Delete Unwanted Pictures and set Duration
* After downloading the images you need to go into the download folder and MANUALLY delete any image you do not want.
* After you have MANUALLY deleted all the images you do not want type ```1``` on the command prompt.
* After that select the duration of each image during the video.

![The game](https://i.imgur.com/gbS7zUb.png)

### Rendering the video
* The program then will take a while to render your video.
* The final video will be in the same directory of the project and will be called ```movie.mp4```
