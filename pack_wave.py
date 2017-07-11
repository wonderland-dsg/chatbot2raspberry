#coding:utf-8

from sys import byteorder
from array import array
from struct import pack

import mywave as wave
import wave as swave


THRESHOLD = 400
CHUNK_SIZE = 1024
RATE = 8000

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    #print "max snd_data",max(snd_data)
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def pack2wavefile(data,sample_width=2,path="just_text.wav"):
    "Records from the microphone and outputs the resulting data to 'path'"
    data = normalize(data)
    data = trim(data)
    data = add_silence(data, 0.5)

    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    sound_file=wf.writeframes(data)

    '''swf=swave.open('wavetest.wav', 'wb')
    swf.setnchannels(1)
    swf.setsampwidth(sample_width)
    swf.setframerate(RATE)
    swf.writeframes(data)
    swf.close()'''

    myfile=open(path, 'wb')
    myfile.write(sound_file.get_buffer())
    myfile.close()
    res=array('h')
    res.extend(sound_file.get_buffer())
    print "pack_wave data len:",len(res),"data len:",len(data)
    wf.close()
    return res