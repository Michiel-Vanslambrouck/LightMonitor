# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:23:00 2018
Python 3.6
@author: Michiel
"""

from PIL import Image
import glob
import re
import datetime
DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']

def light(a): return a[0]+a[1]+a[2]

def evalsquare(pixels,x1,x2,y1,y2):
    score = 0
    score += sum(light(pixels[x,y]) for y in range(y1,y2) for x in range(x1,x2))
    score = score/((x2-x1)*(y2-y1)*(3*255)) #scaling to [0-1] 
    return score

def evalpic(path):
    pic=Image.open(path)
    pixels=pic.load()
    
    date = DayL[datetime.date(int(path[14:16]),int(path[16:18]),int(path[18:20])).weekday()] + 'day'
    
    score0=evalsquare(pixels,0,20,0,20) #sky color analyze
    score1=evalsquare(pixels,170,184,123,150)
    score2=evalsquare(pixels,131,145,123,150)
    score3=evalsquare(pixels,92,108,123,150)
    score4=evalsquare(pixels,58,70,123,150)
    score5=evalsquare(pixels,20,34,123,150)
    
    #name=re.sub("-","",str(path[14:25]))
    #pic.save('.\\teverwerken\\' + name + '.jpg')
    #print('saved .\\teverwerken\\' + name + '.jpg')
    
    pic.close()

    guess1='1' if score1>0.2 else '0'
    guess2='1' if score2>0.2 else '0'
    guess3='1' if score3>0.2 else '0'
    guess4='1' if score4>0.2 else '0'
    guess5='1' if score5>0.2 else '0'

    numeric.write(str(path[14:25]+' '+str(score0)[0:4]+' '+str(score1)[0:4]+' '+str(score2)[0:4]+' '+str(score3)[0:4]+' '+str(score4)[0:4]+' '+str(score5)[0:4]+'\n'))
    if score0 < 0.5:
        guess.write(str(path[14:25]+' '+guess1+' '+guess2+' '+guess3+' '+guess4+' '+guess5+' '+date+' '+str(path[21:23])+'\n'))
    return
    
directory = r'.\teverwerken\*.jpg'
numeric=open(r'results.txt','w')
guess=open(r'guess.txt','w')
files = list(glob.glob(directory))
[evalpic(files[i]) for i in range(0,len(files))]
numeric.close()
guess.close()




