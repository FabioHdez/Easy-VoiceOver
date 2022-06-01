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

![Selecting topic and images](https://user-images.githubusercontent.com/44535804/171313642-c6bf99ba-0609-46df-9649-8e03f88bb5dd.png)

### Delete Unwanted Pictures and set Duration
* After downloading the images you need to go into the download folder and MANUALLY delete any image you do not want.

![delete unwanted](https://user-images.githubusercontent.com/44535804/171313795-9f1c2174-00ac-4447-9264-1755931fdb33.png)

* After you have MANUALLY deleted all the images you do not want type ```1``` on the command prompt.
* After that select the duration of each image during the video.

![deleting](https://user-images.githubusercontent.com/44535804/171313761-853b5bc0-84a9-4103-b5f2-4335d1744084.png)

### Rendering the video
* The program then will take a while to render your video.
* The final video will be in the same directory of the project and will be called ```movie.mp4```

![output](https://user-images.githubusercontent.com/44535804/171313826-7ea88564-aa5a-4f77-9d0a-d5a70bc082e4.png)
