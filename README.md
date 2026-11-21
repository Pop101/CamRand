# CamRand

A webcam experiment: capture an image and turn its pixel data into numbers. It is not a cryptographic random number generator.

![CamRand camera artwork](static/assets/img/camrandom.png)

## Table of Contents

- [Run locally](#run-locally)
- [Technologies](#technologies)

## Run locally

Use Python 3.10 or newer, Poetry, `fswebcam`, and a compatible camera. From the repository root:

```sh
poetry install
poetry run python webapp.py
```

Open `http://127.0.0.1:4848`. The script binds to all network interfaces, so only run it where you intend to expose the service. If it returns zeros, check that `fswebcam` can capture images locally. Current camera/runtime compatibility was not tested.

## Technologies

- [Flask](https://flask.palletsprojects.com/) and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) serve the web app.
- [fswebcam](https://github.com/fsphil/fswebcam) captures images.
- [Pillow](https://python-pillow.org/), [NumPy](https://numpy.org/), and [Cython](https://cython.org/) process pixels.
