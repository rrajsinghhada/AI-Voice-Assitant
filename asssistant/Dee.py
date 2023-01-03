#  Import the required module for text 
# to speech conversion

import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
import wave
# init function to get an engine instance for the speech synthesis
import webbrowser
import smtplib
from playsound import playsound as ps
from googletrans import Translator as trans
from gtts import gTTS as gt
from pydub import AudioSegment
from pydub.playback import play
# from config.definitions import ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

engine = pyttsx3.init()
#Enter the name and there respective email address to send them email
contact_info = {'harry':'harry295@gmail.com','rishi':'rishi123@gmail.com','papa':'sssan@gmail.com','nishu jija':'shrixyz@gmail.com'}
#languages to choose from
dic_language = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian'
'bs', 'bulgarian', 'be', 'catalan', 'ca',
'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
'Zh-cn', 'chinese', 'Zh-tw',
'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
'da', 'dutch', 'nl','english', 'en', 'esperanto',
'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
'french', 'fr', 'frisian', 'fy', 'galician', 'g!',
'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati'
'gu', 'haitian creole', 'ht', 'hausa', 'ha',
'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong',
'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
'lb', 'macedonian', 'mk', 'malagasy',
'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
'mi', 'marathi', 'mr', 'mongolian', 'mn',
'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no'
'odia', 'or', 'pashto', 'ps', 'persian',
'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
'romanian', 'ro', 'russian', 'ru', 'samoan',
'sm', 'scots gaelic', 'ed', 'serbian', 'st', 'sesotho',
'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so',
'spanish', 'es', 'sundanese', 'su',
'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
'ukrainian', 'uk', 'urdu', 'ur', 'uvshur', 'us', 'uzbek',
'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
'yiddish', 'vi', 'yoruba', 'vo', 'zulu', 'zu')

#Saving the Path of the sound in variable for use 
listening_sound = os.path.join(ROOT_DIR, 'sound', 'ding.wav')
did_not_get = os.path.join(ROOT_DIR, 'sound', 'mixkit-software-interface-back-2575.wav')
translated_audio = os.path.join(ROOT_DIR, 'sound', 'Downloadscaptured_jtp_voice.mp3')


# say method on the engine that passing input text to be spoken
def speak(audio):
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine. setProperty("voice", voice_id)
    # Here you can change the rate of the assistant 
    engine. setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        str = 'Good morning'
    elif hour>=12 and hour<16:
        str = 'Good Afternoon!'
    else:
        str = 'Good Evening!'
    

    speak(f'{str} ,I am dee. How may I help you.')

   

def takecommand():
    #it takes microphone input from the user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        song = AudioSegment.from_mp3(listening_sound)
        play(song)
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source) 
    
    try:
        print('Recognizing.....')
        query = r.recognize_google(audio,language ='en-in')
        print('user said: ',query,'\n')
        
    except Exception as e:
        print(e)
        song = AudioSegment.from_mp3(did_not_get)
        play(song)
        print('Say that again please....')
        return 'None'
    return query

def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #Here you have to give your email credentials but in place of password you have to right the security code which is generated after you allow two way security
    server.login('enter your email here @gmail.com','enter your password')
    server.sendmail('enter your email @gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wish_me()
    while True:
        query = takecommand().lower()
        
        if 'please' in query:
            speak('With pleasure')
            
        if 'wikipedia' in query:
            print('searching.....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('according to wikipedia')
            speak(results)
            break
        #here i have given the link for my fav song you can always use this to give the directory of the folder containing the songs
        elif ('play music' or 'song') in query:
            webbrowser.open('https://www.youtube.com/watch?v=1lmSuckzzJ0')
            break   
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            break
        
        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
            break
        
        elif ' time' in query:
            strTime = datetime.datetime.now().strftime(' %H:%M:%S')
            print(strTime)
            speak(f'sir the time is {strTime}')
            break
        elif 'email' in query:
            for names in contact_info.keys():
                print(names)
                if names in query:
                    break
            if names not in query:
                speak('contact details missing or give the name of the reciever')
                pass
            if names in query:
                try:
                    speak('what should I say?')
                    content = takecommand()
                    while content == 'None':
                        content = takecommand()
                    to = contact_info[names]
                    send_email(to,content)
                    speak('email has been sent.')
                except Exception as e:
                    print(e)
                    speak('sorry my friend.unfortunately,there was some problem')
        
        elif 'translate' in query:
            speak('in which language do you want me to translate . Speak only the name of the language.')
            lag = takecommand()
            while lag == 'None':
                lag = takecommand()
            lag = lag.lower()
            while lag not in dic_language:
                speak('the language is currently not in the system if you want translate in some other language give the name')
                
                lag = takecommand()
                lag = lag.lower()
            lag = dic_language[dic_language.index(lag)+1]
            speak('speak the sentance you want to translate.')
            query1 = takecommand()
            while query1 == 'None':
                query1 = takecommand()
            translator1 = trans()
            print(lag,query1)
            text_to_translate_1 = translator1.translate(query1,src = 'en',dest = lag)
            text_1 = text_to_translate_1.text
            spek = gt(text=text_1, lang=lag, slow=False)
            spek.save(translated_audio)
            ps(translated_audio)
            # song = AudioSegment.from_mp3(translated_audio)
            # play(song)
            os.remove(translated_audio) 
        elif 'how are you' in query:   
            speak('I am excellent')
        
        elif 'thank you' in query:
            speak('It was a pleasure to help you.')
            break            
            # print(text)
            





 

