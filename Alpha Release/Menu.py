#imports libaries
import os
import speech_recognition as sr
from gtts import gTTS


#sets welcome message to be converted into speech audio, saved and then opened
welcometext = "say face to open up facial recognition, new user to make a new profile or rock paper scissors to play rock paper scissors"
language = 'en'
myobj = gTTS(text=welcometext, lang=language, slow=False)
myobj.save("welcome1.mp3")
os.system("welcome1.mp3")

# r is set as the speech recognizer
r = sr.Recognizer()
#source is set as what is passed through the microphone
with sr.Microphone() as source:
    #prompted say your choice and audio is set as your answer
    print("say your choice and wait")
    audio = r.listen(source)
#"option" is set as what google recognizes the sound to be otherwise the correlating error is printed 
try:
    print("You said: " + r.recognize_google(audio))
    
    option = r.recognize_google(audio)
    option = option.lower()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#if the word "face" is said the face recognition program is ran
if option == "face":
    import facerecognition
    exec(open('facerecognition.py').read())
#if the words "rock paper scissors" is said the rock paper scissors program is ran
elif option == "rock paper scissors":
    import SpeechRPSv3
    exec(open('SpeechRPSv3.py').read())
#if the words "new user" is said the face trainer program is ran
elif option == "new user":
    import trainer
    exec(open('trainer.py').read())
else:
    print("error the option you selected wasn't recognised as a valid anwser")
