import os
from PIL import Image
from decimal import Decimal
import subprocess

class RandomImageSource:
    def __init__(self):
        self.last_random = 0
        self.last_random = self.get_seed()
    
    def color_algo(self, pxs:tuple):
        return ''.join(map(lambda x: str(bin(x)).replace('b',''), pxs))

    def gray_algo(self, pxs:tuple):
        gray = int(sum(pxs) / len(pxs))
        return str(bin(gray)).replace('b','')
    
    def bw_algo(self, pxs:tuple):
        gray = sum(pxs) / len(pxs)
        return "1" if gray > 127.5 else "0"
    
    def get_seed(self, algorith=None):
        if algorith == None: algorith = self.gray_algo

        captureImage = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "static.jpg"]) # change this line to             captureImage = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "static.jpg", "--skip", "10"])     if you have an older camera.                                                                               #captureImage = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "static.jpg", "--skip", "10"])
        captureImage.communicate()

        img = Image.open("./static.jpg")
        px = img.load()

        rand = ""
        for x in range(img.width):
            for y in range(img.height):
                rand += algorith(px[x, y])
        
        rand_int = int(rand, 2) - self.last_random
        self.last_random = int(rand, 2)
        return rand_int if rand_int > 0 else -rand_int

    def get_random(self):
        seed = self.get_seed()
        return Decimal(seed) / Decimal(int("1" * len(str(bin(seed))) ,2))
    
if __name__ == '__main__':
    source = RandomImageSource()
    seed = source.get_seed()
    print(seed)
    print(float(source.get_random()))

    import hashlib
    print(int(hashlib.sha3_224(str(seed).encode('utf-8')).hexdigest(), 16))