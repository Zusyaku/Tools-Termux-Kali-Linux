#!/usr/bin/env python3
#Give it a wav file and it will convert it to text file for you
import speech_recognition as sr
import sys
try:
    wav_file = sys.argv[1]
except:
    wav_file = input("Wav file (Make sure it's in the same dir) ->")
r = sr.Recognizer()
with sr.AudioFile(wav_file) as source:
    audio = r.record(source)
try:
    print("Sphinx read : \n" + r.recognize_sphinx(audio))
except:
    print("Sphinx error!")
print("--------------------------------")

try:
    print("Google Speech Recognition read :\n" + r.recognize_google(audio))
except:
    print("Google Speech Recognition service!")
