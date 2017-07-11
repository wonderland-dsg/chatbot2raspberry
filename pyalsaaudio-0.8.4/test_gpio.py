#coding:utf-8
import RPi.GPIO as GPIO    
import time    
# BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
# 输出模式    
GPIO.setup(7, GPIO.IN)    
     
while True:    
    time.sleep(1)
    if GPIO.input(7):
        print('Input was HIGH')
    else:
        print('Input was LOW')
