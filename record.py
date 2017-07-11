#!/usr/bin/env python
#coding:utf-8
## recordtest.py
##
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm device for sound capture, sets
## various attributes of the capture, and reads in a loop,
## writing the data to standard out.
##
## To test it out do the following:
## python recordtest.py out.raw # talk to the microphone
## aplay -r 8000 -f S16_LE -c 1 out.raw

#!/usr/bin/env python

from __future__ import print_function

import sys
import time
import getopt
import alsaaudio

def usage():
    print('usage: recordtest.py [-d <device>] <file>', file=sys.stderr)
    sys.exit(2)

if __name__ == '__main__':

    device = 'default'

    opts, args = getopt.getopt(sys.argv[1:], 'd:')
    for o, a in opts:
        if o == '-d':
            device = a

    if not args:
        usage()

    f = open(args[0], 'wb')

    # Open the device in nonblocking capture mode. The last argument could
    # just as well have been zero for blocking mode. Then we could have
    # left out the sleep call in the bottom of the loop
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)

    # Set attributes: Mono, 44100 Hz, 16 bit little endian samples
    inp.setchannels(1)
    inp.setrate(16000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(500)
    # The period size controls the internal number of frames per period.
    # The significance of this parameter is documented in the ALSA api.

    # For our purposes, it is suficcient to know that reads from the device
    # will return this many frames. Each frame being 2 bytes long.
    # This means that the reads below will return either 320 bytes of data
    # or 0 bytes of data. The latter is possible because we are in nonblocking
    # mode.
    inp.setperiodsize(160)

    loops = 1000000
    while loops > 0:
        loops -= 1
        # Read data from device
        l, data = inp.read()

        if l:
            f.write(data)
            time.sleep(.001)



#coding:utf-8
import RPi.GPIO as GPIO
import time
from array import array

def record():
    # BOARD编号方式，基于插座引脚编号
    GPIO.setmode(GPIO.BOARD)
    # 输出模式
    GPIO.setup(7, GPIO.IN)

    #device = 'default'
    device='plughw:CARD=Device,DEV=0'#'hw:CARD=sndrpihifiberry,DEV=0'



    while(GPIO.input(7)==1):
        pass

    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)

    # Set attributes: Mono, 16000 Hz, 16 bit little endian samples
    inp.setchannels(1)
    inp.setrate(16000)
    inp.setperiodsize(800)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    sound=array('h')
    while(GPIO.input(7)==0):
        l, data = inp.read()
        if l:
            print( "record...")
            print(type(data))
            #data=[ord(s) for s in data]
            #print(data)
            if 1:
                #insert_unit=ord(insert_unit)
                print("string!")
                temp=array('h')
                temp.fromstring(data)
                data=temp
            sound.extend(data)
            time.sleep(.001)
    return sound
