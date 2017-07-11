import chat
import os
import wave
import record
if __name__ =='__main__':
    chatbot=chat.cRobot()
    while(True):
        str = raw_input("Enter your input: ")
        if(str=='q'):
            print "finished!"
            break
        print str

        #os.system('arecord -D "plughw:1,0" -f S16_LE -d 5 -r 8000 d.wav')
        #fp=wave.open("d.wav",'rb')
        #nf=fp.getnframes()
        #f_len=nf*2
        #audio_data = fp.readframes(nf)

        sound=record.record()
        s_len=len(sound)
        res_mp3=chatbot.chat(sound,s_len*2)
        f2=file(r"hhh.mp3",'w')
        f2.write(res_mp3)
        f2.close()
        os.system('play hhh.mp3')
