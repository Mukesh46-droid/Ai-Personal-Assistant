import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia 

#Initialize the TTS engine
engine = pyttsx3.init()

# Function to convert text to speech 
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Function to recognize speech 
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command=recognizer.recognize_google(audio)
            print(f"User said:{command}")
            return command.lower()
        except Exception as e:
            print("Sorry, I could not understand.")
            return ""
        
        def greet():
            hour=int(datetime.datetime.now().hour)
            if hour < 12:
                speak("Good morning")
            elif hour < 18:
                speak("Good afternoon!")
            else:
                speak ("Good evening!")
            speak("How can I assist you?")
            
        def tell_time():
            current_time = datetime.datetime.now().strftime("%I: %M %p ")
            speak(f"The time is {current_time}")
            
        def search_wikipedia(query):
            speak("Searching Wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            
        def open_website(url):
            speak(f"Opening {url}")
            webbrowser.open(url)
            
        def personal assistant():
            greet()
            while True:
                command = listen()
                
                if 'time' in command:
                    tell_time()
                    
                elif 'wikipedia' in command:
                    speak("What should I search on Wikipedia?")
                    query = listen()
                    search_wikipedia(query)
                    
                elif 'open' in command:
                    if 'google' in command:
                        open_website("https://www.google.com")
                elif 'youtube' in command:
                    open_website("https://www.youtube.com")
                    
                                
elif 'exit' in command or 'stop' in command:
    speak("Goodbye!")
    break

if_name_=="_main_":
    personal_assistant()        
                    
                        
                        
             
                
            
           
                         
                       
        
        
            