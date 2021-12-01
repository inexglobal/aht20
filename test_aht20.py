import gc
gc.collect()
from microbit import i2c,sleep
from AHT20 import *
a = AHT20()
while 1:
    sleep(1000)
    t,h = a.read()
    print(t,h)
