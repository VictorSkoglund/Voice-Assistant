import speech_recognition as sr
from gtts import gTTS
import os
import playsound as ps

name = 'Repeater'

def speak(output):
    print("{}: {}".format(name,output))
    tts = gTTS(output, lang='en')
    tts.save('output.mp3')
    ps.playsound('output.mp3', True)
    os.remove('output.mp3')

def listen():
    r = sr.Recognizer()
    audio = ''
    
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)
        print("Stop.")
        phrase = r.recognize_google(audio)
        print("You: ", phrase)
        return phrase

def main():
    while(1):
        speak("Hello, I'm {}, what can i repeat for you?".format(name))
        text = listen().lower()
        speak(text)
        if "bye" in str(text):
            print("Good bye!")
            break

if __name__ == "__main__":
    main()
