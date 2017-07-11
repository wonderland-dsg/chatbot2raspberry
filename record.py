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
