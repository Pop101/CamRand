import os, hashlib
from PIL import Image
from decimal import Decimal
import numpy as np
import subprocess
import pyximport; pyximport.install()

def hash_to_int(obj):
    return int(hashlib.sha512(repr(obj).encode('utf-8')).hexdigest(), 16)

def numberToBase(n:int, b:int = -1, key:str or list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"):
    if(b == -1): b = len(key)
    digits = ""
    while n:
        digits += key[int(n % b)]
        n //= b
    return digits

class RandomImageSource:
    def __init__(self, take_picture=True):
        self.take_picture = take_picture
        self.last_random = 0
        if take_picture: self.last_random = self.get_seed()

    def color_algo(self, pxs:tuple):
        return ''.join(map(lambda x: str(bin(x))[2:], pxs))

    def gray_algo(self, pxs:tuple):
        gray = int(sum(pxs) / len(pxs))
        return str(bin(gray))[2:]

    def bw_algo(self, pxs:tuple):
        gray = sum(pxs) / len(pxs)
        return "1" if gray > 127.5 else "0"

    def get_raw_int(self, algorith=None):
        if algorith == None: algorith = self.gray_algo

        if self.take_picture:
            captureImage = subprocess.Popen(['ffmpeg', '-f', 'video4linux2', '-i', '/dev/video0', '-vframes' '1', 'static.jpg'])
            captureImage.communicate()

        img = Image.open("./static.jpg").convert("RGB")
        px = np.array(img).reshape(-1,3)
        rand =  ''.join(list(map(algorith, px)))

        rand = int(rand, 2)
        self.last_random = rand
        return rand

    def get_seed(self, algorith=None, threshold:int = 10000):
        rand_int = self.last_random - self.get_raw_int(algorith=algorith)
        if -threshold < rand_int < threshold: return self.last_random # do this to avoid returning 0
        else: return rand_int if rand_int > 0 else -rand_int # only return positive numbers

    def get_random(self):
        seed = self.get_seed()
        return Decimal(seed) / Decimal(int("1" * (len(str(bin(seed))) - 1), 2))

if __name__ == '__main__':
    source = RandomImageSource()
    print(source.get_raw_int())
    
    seed = source.get_seed()
    print(seed)
    print(float(source.get_random()))
