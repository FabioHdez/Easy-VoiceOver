from google_images_download import google_images_download
from moviepy.editor import *
import os

def main():
    topic = download()
    deleteUnwanted(topic)

# Download Images
def download():
    topic = input("Enter the topic: ")
    numOfPics = input("How many pictures do you want?: ")
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":topic,"limit":numOfPics}
    paths = response.download(arguments)
    return topic

# User deletes unwanted pictures before proceeding
def deleteUnwanted(topic):
    selecting = input("Please delete unwanted pictures, type '1' when finished: ")
    if selecting != "1":
        deleteUnwanted()
    elif selecting == "1":
        duration = input("Duration per image?(in seconds): ")
        createVid(int(duration),topic)

# Create Array of images to create vid
def createVid(duration,topic):
    clipsArr = []
    imgs = os.listdir('downloads/'+topic)
    for img in imgs:
        clip = ImageClip("downloads/"+topic+"/"+img)
        clip = clip.resize( (1920,1080) )
        clip = clip.set_duration(t = duration)
        clipsArr.append(clip)
    finalClip = concatenate_videoclips(clipsArr)
    finalClip.write_videofile("movie.mp4",audio=False,fps = 24)
    
if __name__ == '__main__':
    main()
