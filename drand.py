import pyximport; pyximport.install()
from camrand import hash_to_int, numberToBase
from camrand import RandomImageSource

source = RandomImageSource()
source.last_call = time.time()

value = hex(source.get_seed())[2:]

print(value)