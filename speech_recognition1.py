                                               # NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print('say something...')                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        text=r.recognize_google(audio)

        if text in "hello":
         print("That is great!, How are you ? ")
        elif text in ["i am fine", "i am good", "good"]:
            print("nice to meet you ")
        elif text in "close":
           sys.exit(0)
        else:
            print("I don't understand")