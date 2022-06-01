# Easy-VoiceOver
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to play](#how-to-play)

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
$ py main.py
```

## How to Use
### Starting the Game
* First enter the number of players and the name of each player.
* The first player will choose a starting piece.
* To choose a piece you need to input the index of your desired piece.

![Starting the game](https://i.imgur.com/v91OK1u.png?1)


### The Game
* The rules of the game are available at https://www.coololdgames.com/tile-games/dominoes/cuban/
* Each turn you will be able to play a piece by inputting the index of your desired piece.
* The image below shows the table, player's pieces and the turn number.

![The game](https://i.imgur.com/gbS7zUb.png)

### Winning the Game
* The game will end when none of the players can play any pieces or when a player runs out of pieces.
