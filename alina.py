import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from flask import Flask,render_template, Response, stream_with_context

app = Flask(__name__)
def alinaapp():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Hi Master  Good Morning!   Its been quite a while Hope Your night was spent well!")

        elif hour>=12 and hour<18:
            speak(" Hi Master Good Afternoon! How are you Its been a While  Waiting for your command")

        else:
            speak(" Hi BOSS Good Evening!Hope your evening was well")

        speak(" I am Alina  at your work BOSS , I am here to make your work easier. ")
        speak("Is there anything that I can do for you")

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        BOSS = "cheif"
        with sr.Microphone() as source:
            speak("Listening to your command %s" % BOSS)
            print("Listening to your command %s" % BOSS)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            speak("Recognized the command BOSS  Working on it")
            print("Recognized the command BOSS  Working on it")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            speak("Pardon %s can you repeat your command" % BOSS)
            print("Pardon %s can you repeat your command" % BOSS)
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()


    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "what's the market saying today" in query:
            webbrowser.open("https://www.moneycontrol.com/")
        elif 'check my Instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'play hindi songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=hindi+songs")
        elif 'play english songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=english+songs")
        elif 'play taylor swift songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=taylor+swift+songs")
        elif 'play selena gomez songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=selena+gomez+songs")
        elif 'play hindi movies' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=hindi+movies")
        elif 'open vaccine site' in query:
            webbrowser.open("https://www.cowin.gov.in/")
        elif 'open my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?pli=1#inbox")
        elif 'open list of actors' in query:
            webbrowser.open("https://www.imdb.com/list/ls068010962/")
        elif  'open rich people list' in query:
            webbrowser.open("https://www.forbes.com/india-billionaires/list/")
        elif 'open shopping site' in query:
            webbrowser.open("https://www.amazon.in/")
        elif 'open my classroom for assignment'in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif "open today's market" in query:
            webbrowser.open("https://www.moneycontrol.com/")
        elif 'current bitcoin price ' in query:
            webbrowser.open("https://www.google.com/search?q=bitcoin&oq=bitcoin&aqs=chrome..69i57.2685j0j1&sourceid=chrome&ie=UTF-8")
        elif 'I am bored ' in query:
            speak("Do you want to here a joke Ohh probably I will open a joke website for you.")
            webbrowser.open("https://in.pinterest.com/ohyaaro/funny-jokes/")
        elif 'Open C Drive' in query:
            os.startfile('C:\ ')


        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'exit alina' in query:
            speak("By chief see you later, Have a good time. ")
            exit()



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif ' love you Siri' in query:
            strhate = ("Hate u")
            speak("Hate u master , I was always loyal to u , ok byee. I was hurt , But unfortunetly I have to take another command see ya")




        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)


        elif 'email to Aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend ")
            
@app.route('/')
def hello():
    return render_template('Alina.html')

@app.route('/output')
def output():
    # return alinaapp()
    return Response(stream_with_context(alinaapp()))

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0 ')