# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:39:45 2024

@author: dell
"""
import speech_recognition as sr
AUDIO_FILE=("harvard.wav")
#use audio file as source
r=sr.Recognizer()#intialise the recogniser
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    #reads the audio file
try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recgnition could not understand audio")
except sr.RequestError:
    print("Couldn't get result")