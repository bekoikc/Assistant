import datetime
import os
import random
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import time
import winsound
import keyboard



# speech engine initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 male 1 = female
activationWord = 'jarvis'


# Youtube music link
ytMusiclink = r"https://music.youtube.com/playlist?list=PL4LtaZuYCvhsumxWF7jQj9iouTXL5zT6k"

# Spotify Path
spotiPath = r"C:\Users\bekob\AppData\Roaming\Spotify.exe"

# Welcome Words
welcomeWords = ['Hello Sir!', 'What would you like me to do today?', 'What would you like?', 'How are you sir', 'What do you want me to do right now?']
randomWelcomeWords = random.choice(welcomeWords)

# Configure browser
# set the path
opera_path = r"C:\Users\bekob\AppData\Local\Programs\Opera\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))

# notepad path
notepad_path = r"G:\Assistan\notepad.py"

# Wolfrom alpha  client
appId = 'HEW2PG-TQXWARELA7'
wolfromClient = wolframalpha.Client(appId)


# Run other python files
def on_key_press(key):
    if key.name == 'f10' and keyboard.is_pressed('shift'):
        pass

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Listening for command')
    speak('Listening for command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)


    try:
        print('Recognizing speech...')
        speak('Analyzing Data')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f"The input speech was: {query}")
    except Exception as exception:
        print('Sorry I did not quite catch that')
        speak('Sorry. I did not quite catch that')
        print(exception)
        return 'None'

    return query

def search_wikipedia(query = ''):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('Sorry.No wikipedia result')
        return 'No results Received'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
        print(wikiPage.title)
        wikiSummary = str(wikiPage.summary)
        return wikiSummary
#Main loop
if __name__ == '__main__':
    speak('All systems nominal.')
    speak(randomWelcomeWords)

    while True:
        # Parse as a list
        query = parseCommand().lower().split()
        if query[0] == activationWord:
            query.pop(0)

            # Navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('opera').open_new(query)

            # Wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal DataBank.')
                speak(search_wikipedia(query))

            # Play Music
            if query[0] == 'play' or query[1] == 'music':
                speak('Opening Spotify Sir')
                os.open(spotiPath)

            # Search Eray on Youtube
            if query[0] == 'funny' or query[1] == 'videos':
                speak('Opening Eray Sir')
                webbrowser.get('opera').open_new("https://www.youtube.com/@erayozkenar/videos")

            # Notepad writing
            if query[0] == 'notepad':
                speak('opening notepad')
                os.open(notepad_path)



            # EXIT
            if query[0] == 'exit':
                speak('Goodbye Sir')
                break