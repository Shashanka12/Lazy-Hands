import speech_recognition as sr
from googlesearch import search
def sp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        print("Input found to be: " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sorry! Couldn't get you")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    '''
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    '''
    '''try:
        from google import search
    except ImportError: 
        print("No module named 'google' found")
    ''' 

    # to search
    query = r.recognize_sphinx(audio) 
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        print(j)
