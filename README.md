# CamRand
CamRand is a flask program to generate random numbers off of a image taken by a camera.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Sites](#see-it-in-action)

## General Info
CamRand creates its random numbers by taking a picture using FsWebcam. It then iterates over the picture's pixels to create a string of bits. This string is then hashed and compared to the previous seed. Thus, CamRand assures the creation of unique seeds. \
If you keep getting 0s, make sure you have FsWebcam properly installed and have your camera facing some kind of entropy source. Any further issues should go in issues.

## Technologies
This project is created with:
* [Flask](flask.palletsprojects.com): 1.1.2
* [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/): 1.4.4
* [Pillow](https://python-pillow.org/): 8.0.1
* [Cython](https://cython.org): 0.29.21
* [FsWebcam](https://github.com/fsphil/fswebcam): 20200725

## See it in Action
<img src="https://github.com/Pop101/CamRand/blob/main/static/assets/img/camrandom.png?raw=true" width="2%"></img>
[rand.leibmann.org](https://rand.leibmann.org) \
<img src="https://github.com/Pop101/CamRand/blob/main/static/assets/img/camrandom.png?raw=true" width="2%"></img>
[rand.tennisbowling.com](https://rand.tennisbowling.com)

## Setup
Clone the Repo \
```git clone https://github.com/Pop101/CamRand``` \
Install fswebcam\
```sudo apt update && sudo apt install fswebcam``` \
Enter the Repo and Install requirements \
```cd CamRand && sudo python3 -m pip install -r requirements``` \
Run the app! \
```sudo python3 webapp.py``` \
That's it! you can access it at \
```your-ip-here:1000```




