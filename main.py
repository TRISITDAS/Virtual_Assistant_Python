import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os

import wikipedia
import yfinance as yf
import pyjokes

# listen to our microphone and return the audio as text using google
import speech_recognition as sr


def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening")
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry i Did not Understand")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry the service is down")
            return "I am waiting"
        except:
            return "I am waiting"


# transform()
def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


# speak('hello world')
engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#     print(voice)
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', id)
# engine.say('Hello TRISIT DAS')
engine.runAndWait()


# return the week day name
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    try:
        speak(f'Today is {mapping[weekday]}')
    except:
        pass


query_day()


# return the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"{time[0:2]} o' clock and {time[3:5]} minutes")


query_time()


# intro greeting as startup
def whatsup():
    speak('''Hi, My name is Elia. I am your personal Assistant created by TRISIT.
    How may i help you?
    ''')


# whatsup()


# the heart of our assistant. Takes queries and return answers
def querying():
    whatsup()
    start = True
    while start:
        q = transform().lower()

        if 'open youtube' in q:
            speak('Starting Youtube in Seconds..')
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'open web browser' in q:
            speak('Starting Web Browser in Seconds.')
            webbrowser.open("https://www.google.com")
            continue

        elif 'what day is it' in q:
            query_day()
            continue

        elif 'tell me the time' in q:
            query_time()
            continue

        elif 'switch it off' in q:
            speak('i am shutting down. bye. ')
            break

        elif 'search wikipedia' in q:
            speak('checking WIKIPEDIA')
            q = q.replace("wikipedia", "")
            result = wikipedia.summary(q, sentences=2)
            speak('found on wikipedia')
            speak(result)
            continue

        elif "your name" in q:
            speak('i am elia. Your Virtual Assistant')
            continue

        elif "search web" in q:
            pywhatkit.search(q)
            speak('that is what i found')
            continue

        elif "play" in q:
            speak(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
        elif "joke" in q:
            speak(pyjokes.get_joke())
            continue

        elif "stock price" in q:
            search = q.split("of")[-1].strip()
            lookup = {'apple': 'AAPL',
                      'amazon': 'AMZN',
                      'google': 'GOOGL'}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speak(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speak(f'sorry i have no data for {search}')
            continue


querying()
