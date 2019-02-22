# work a PIR
# incidentally, PIR outputs 3.3V on data pin even if it's powered by 5v - cool.
# Let's get some fun audio clips from http://www.moviewavs.com 
#
import mp3
from utime import sleep
import urandom
BITS = 2   # for a total of 4 songs
mp3.set_volume(25)

def main():
        from machine import Pin, Signal
        from utime import sleep

        pin = Pin(0, Pin.IN)   # set GPIO4 as input with pullup
        pir = Signal(pin, invert=False)   # let's use Signals, eh?
        detected = False
        while True:
                if not detected and pir.value():  # gone HIGH
                        print("A Visitor!")
                        mp3.play_track(urandom.getrandbits(BITS)+1)        # since the MP3 doesn't recognize song 0
                        detected = True
                elif detected and not pir.value():   # gone LOW
                        print("Bye!")
                        detected = False
                        sleep(60*20)      # sleep 20 minutes
