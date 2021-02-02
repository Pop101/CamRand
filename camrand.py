import os, hashlib
from PIL import Image
from decimal import Decimal
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
    def __init__(self):
        self.last_random = 0
        self.last_random = self.get_seed()
    
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

        captureImage = subprocess.Popen(['fswebcam',  '--no-banner', 'static.jpg'], stderr=subprocess.DEVNULL) # redirect output to /dev/null for drand.py
        captureImage.communicate()

        img = Image.open("./static.jpg")
        px = img.load()

        rand = ""
        for x in range(img.width):
            for y in range(img.height):
                rand += algorith(px[x, y])
        
        rand = int(rand, 2)
        self.last_random = rand
        return rand
    
    def get_seed(self):
        rand_int = self.last_random - self.get_raw_int(algorith=self.gray_algo)
        return rand_int if rand_int > 0 else -rand_int

    def get_random(self):
        seed = self.get_seed()
        return Decimal(seed) / Decimal(int("1" * (len(str(bin(seed))) - 1), 2))
    
if __name__ == '__main__':
    source = RandomImageSource()
    seed = source.get_seed()
    print(seed)
    print(float(source.get_random()))