import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# speech engine initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 male 1 = female
activationWord = 'jarvis'

# Configure browser
# set the path
opera_path = r"C:\Users\bekob\AppData\Local\Programs\Opera\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))

# Wolfrom alpha  client
# appId = 'HEW2PG-6GVE36P6HV'
# wolfromClient = wolframalpha.Client(appId)

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

    while True:
        # Parse as a list
        query = parseCommand().lower().split()
        if query[0] == activationWord:
            query.pop(0)

            #list commands
            if query[0] == 'say':
                if 'everything is okey' in query:
                    speak('Greating, all sir')
                else:
                    query.pop(0) # Remove Say
                    speech = ' '.join(query)
                    speak(speech)

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

            #Wolfrom Alpha
            # COMIN FUTURE...

            # Note taking
            if query[0] == 'take note':
                speak('Ready to record your note.')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note Written')

            if query[0] == 'exit':
                speak('Goodbye Sir')
                break