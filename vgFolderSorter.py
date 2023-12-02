import os
import sys 
import shutil
import platform
from pathlib import Path

# CONSTs for consistent strings / folders
AUD = "audio"
VID = "videos"
IMG = "images"
DOC = "documents"
MISC = "misc"

# Lists of format types
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv", ".mid", ".mod", ".it")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".mkv")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

doc = (".doc", ".docx", ".eml", ".html", ".asc", ".msg", 
            ".pages", ".rtf", ".txt", ".ipynb", ".log", 
            ".md", ".wps", ".pdf")

# List of 'yes' strings
yes = ("y", "Y", "yes", "Yes", "yEs", "yeS", "YEs",
       "YeS", "yES", "YES", "ye", "yE", "Ye", "YE")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_doc(file):
    return os.path.splitext(file)[1] in doc

def setupFolders():
    if not os.path.exists(AUD):
        os.mkdir(AUD)
    if not os.path.exists(VID):
        os.mkdir(VID)
    if not os.path.exists(IMG):
        os.mkdir(IMG)
    if not os.path.exists(DOC):
        os.mkdir(DOC)
    if not os.path.exists(MISC):
        os.mkdir(MISC)

def sortFolders():

    # Determine what slash should be used
    joiner = "\\"
    if(platform.system == "Windows"):
        joiner = "/"

    for file in os.listdir():
        if Path(file).is_file():
            if is_audio(file):
                shutil.move(file, os.getcwd() + joiner + AUD)
            elif is_video(file):
                shutil.move(file, os.getcwd() + joiner + VID)
            elif is_image(file):
                shutil.move(file, os.getcwd() + joiner + IMG)
            elif is_doc(file):
                shutil.move(file, os.getcwd() + joiner + DOC)
            else:
                shutil.move(file, os.getcwd() + joiner + MISC)

def main():
    # If argument is provided, change directory to the argument
    if len(sys.argv) == 2:
        dir_path = sys.argv[1]
        if not os.path.isdir(dir_path):
            print(f"{dir_path} does not exist.")
        else:
            print(f"Using directory {dir_path}.")
            os.chdir(dir_path)

    # Check to make sure
    userChoice = input(f"Are you sure you want to sort {dir_path}? (y/n) ")
    if(userChoice not in yes):
        print("Canceling sort...")
        return 0

    # Start the proccess of sorting
    print("Sorting...")
    setupFolders()
    sortFolders()
    print("Sorting done!")

if __name__=="__main__": 
    main() 