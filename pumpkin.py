#!/usr/bin/python

import pygame
from blinkt import set_pixel, set_brightness, show, clear, set_all
from random import randint
from time import sleep

def laugh1():
    pygame.mixer.init()
    pygame.mixer.music.load("./soundEffects/evilLaugh1.wav")
    pygame.mixer.music.play()
    sleep(1)

    while pygame.mixer.music.get_busy() == True:
        bright = randint(50,100)/100
        r = 255
        
        x = randint(0,2)
        if x == 1:
            g = 165
        elif x == 2:
            g = 255
        else:
            g = 0
            
        b = 0
        set_brightness(bright)
        set_all(r, g, b)        
        show()

    clear()
    show()
    return;


def laugh3():
    pygame.mixer.init()
    pygame.mixer.music.load("./soundEffects/evilLaugh3.wav")
    pygame.mixer.music.play()
    sleep(.5)

    while pygame.mixer.music.get_busy() == True:
        bright = randint(50,100)/100
        r = 255
        
        x = randint(0,2)
        if x == 1:
            g = 165
        elif x == 2:
            g = 255
        else:
            g = 0
            
        b = 0
        set_brightness(bright)
        set_all(r, g, b)        
        show()

    clear()
    show()
    return;

def scream1():
    pygame.mixer.init()
    pygame.mixer.music.load("./soundEffects/femaleScream1.wav")
    pygame.mixer.music.play()
    sleep(.5)

    while pygame.mixer.music.get_busy() == True:
        bright = randint(50,100)/100
        r = 255
        
        x = randint(0,2)
        if x == 1:
            g = 165
        elif x == 2:
            g = 255
        else:
            g = 0
            
        b = 0
        set_brightness(bright)
        set_all(r, g, b)        
        show()

    sleep(.5)
    clear()
    show()
    return;

def monster1():
    pygame.mixer.init()
    pygame.mixer.music.load("./soundEffects/monster1.wav")
    pygame.mixer.music.play()
    sleep(.5)

    while pygame.mixer.music.get_busy() == True:
        bright = randint(50,100)/100
        r = 255
        
        x = randint(0,2)
        if x == 1:
            g = 165
        elif x == 2:
            g = 255
        else:
            g = 0
            
        b = 0
        set_brightness(bright)
        set_all(r, g, b)        
        show()

    sleep(.75)
    clear()
    show()
    return;

def TRex1():
    pygame.mixer.init()
    pygame.mixer.music.load("./soundEffects/tRex1.wav")
    pygame.mixer.music.play()
    sleep(.5)

    while pygame.mixer.music.get_busy() == True:
        bright = randint(50,100)/100
        r = 0
        
        x = randint(0,1)
        if x == 0:
            g = 0
            b = 255
        else:
            g = 255
            b = 0
            
        set_brightness(bright)
        set_all(r, g, b)        
        show()

    clear()
    show()
    return;
