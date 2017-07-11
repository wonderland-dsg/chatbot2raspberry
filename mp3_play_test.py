'''import ctypes

align=ctypes.CDLL('mp3_decoder.so')

mf=open("test_music.mp3",'rb')

data=mf.read()

i=1024*8
print len(data)
buffer=data[0:1024*8]
align.play_init(buffer,1024*8)
while i<len(data):
    buffer=data[i:i+1024*8]
    align.push_data(buffer,1024*8)
align.play_close()'''


#http://music.163.com/#/song?id=488388731



from omxplayer import OMXPlayer
from time import sleep

file_path_or_url = 'http://music.163.com/#/song?id=488388731'

player = OMXPlayer(file_path_or_url)

# The player will initially be paused

player.play()
sleep(5)
player.pause()

# Kill the `omxplayer` process gracefully.
player.quit()