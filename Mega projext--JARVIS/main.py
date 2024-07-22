import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib

# import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# apikey="b8460345a008458f8533d50c0d97ae0e" ---We will require paid api key to work on this feature


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommands(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():  # Corrected spelling
        webbrowser.open("https://www.linkedin.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)
    # elif ("news" in c.lower()):
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in    &apiKey={apikey}")
    #     if r.status_code==200:
    #         # Parse the JSON response
    #         data = r.json()

    #         # Extract the articles
    #         articles = data.get('articles', [])

    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])

    # else:
    # Let openai handle the request


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommands(command)
        except Exception as e:
            print("ERROR:\n", e)
