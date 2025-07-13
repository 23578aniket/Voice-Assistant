import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as wk
import datetime as dt
import wikipedia
import webbrowser
import pyautogui as py
import random
import calendar
import time
import sqlite3

print("Try saying Assistant or Six")

# Initialization and Configuration
def initialize_engine():
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    return engine

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def get_wake_words():
    return ["assistant", "six", "6"]

# Database setup
def create_db():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT, age INTEGER, sex TEXT, dob TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new user
def add_user_to_db(name, age, sex, dob):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age, sex, dob) VALUES (?, ?, ?, ?)", (name, age, sex, dob))
    conn.commit()
    conn.close()

# Function to check if a user exists
def user_exists(name):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name=?", (name,))
    user = c.fetchone()
    conn.close()
    return user

# Function to get user details
def get_user_details(name):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name=?", (name,))
    user = c.fetchone()
    conn.close()
    return user

# Function to ask user details
def ask_user_details():
    talk("What is your name?")
    name = takeCommand().lower()
    
    if user_exists(name):
        talk("Welcome back.")
        return name
    else:
        talk(f"Hello {name}, it seems you are a new user. Would you like to save your details?")
        confirmation = takeCommand().lower()
        if "yes" in confirmation or "yeah" in confirmation:
            talk("What is your age?")
            age = int(takeCommand())
            talk("What is your sex?")
            sex = takeCommand().lower()
            talk("What is your date of birth? Please say it in the format: day month year.")
            dob = takeCommand().lower()
            add_user_to_db(name, age, sex, dob)
            talk("Your details have been saved. Thank you.")
        else:
            talk("Okay, I will not save your details.")
        return name

def update_user_details():
    talk("Please tell me the name of the user whose details you want to update.")
    name = takeCommand().lower()
    if user_exists(name):
        talk("What would you like to update? You can say age, sex, or date of birth.")
        detail_to_update = takeCommand().lower()
        if detail_to_update == "age":
            talk("What is the new age?")
            new_age = int(takeCommand())
            update_user_in_db(name, age=new_age)
            talk("Age has been updated.")
        elif detail_to_update == "sex":
            talk("What is the new sex?")
            new_sex = takeCommand().lower()
            update_user_in_db(name, sex=new_sex)
            talk("Sex has been updated.")
        elif detail_to_update == "date of birth":
            talk("What is the new date of birth? Please say it in the format: day month year.")
            new_dob = takeCommand().lower()
            update_user_in_db(name, dob=new_dob)
            talk("Date of birth has been updated.")
        else:
            talk("I didn't understand what you want to update.")
    else:
        talk("User not found. Please check the name and try again.")

def retrieve_user_details():
    talk("Please tell me the name of the user whose details you want to retrieve.")
    name = takeCommand().lower()
    user = get_user_details(name)
    if user:
        talk(f"Name: {user[0]}. Age: {user[1]}. Sex: {user[2]}. Date of Birth: {user[3]}.")
    else:
        talk("No details found for this user.")



# Function to tell the current user details
def tell_current_user_details(name):
    user = get_user_details(name)
    if user:
        talk(f"Your name is {user[0]}. You are {user[1]} years old, your sex is {user[2]}, and you were born on {user[3]}.")
    else:
        talk("I don't have any details for you yet.")


# Listening and Responding
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"Master said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't get that.")
        return "None"

def respond_to_wake_words(wake_words):
    query = takeCommand()
    for word in wake_words:
        if word in query:
            print("Assistant is awake!")
            talk("Yes Sire!!!")
            return True
    return False

def greet():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        talk("Good Morning!")
    elif 12 <= hour < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("How may I assist you?")

# Actions
def play_on_youtube(query):
    query = query.replace("play", "").replace("assistant", "")
    print("Playing...")
    talk("Playing..." + query)
    wk.playonyt(query)
    time.sleep(5)
    py.press('enter')
    
def search_on_youtube(query):
    query = query.replace("search", "").replace("assistant", "")
    print("Searching...")
    talk("Searching..." + query)
    wk.search(query)
    time.sleep(5)
    py.press('enter')

def get_time():
    time = dt.datetime.now().strftime("%I:%M %p")
    print("The time is: " f"{time}")
    talk("The time is " + time)

def get_today_date():
    now = dt.datetime.now()
    date_now = dt.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    year_now = now.year
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    ordinals = ["1st", "2nd", "3rd"] + ["{}th".format(i) for i in range(4, 31)]
    if 11 <= day_now <= 13:
        ordinals.append("{}th".format(day_now))
    else:
        ordinals.append("{}{}".format(day_now, {1: 'st', 2: 'nd', 3: 'rd'}.get(day_now % 10, 'th')))
    
    today = f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}, {year_now}'
    print(today)
    talk(today)

def search_on_google(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    
def respond_to_greetings(query):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello", "hey there", "howdy"]
    response = ["hi", "hey", "hola", "greetings", "wassup", "hello", "hey there", "howdy"]
    for word in query.split():
        if word.lower() in greet:
            return random.choice(response)
    return ""

def what_can_you_do():
    print("I can do everything that my creator programmed me to do.")
    talk("I can do everything that my creator programmed me to do.")
    print("How may I help you?")
    talk("How may I help you?")

def respond_to_how_are_you():
    print("I am fine, Thank you")
    talk("I am fine, thank you")

def introduce_assistant():
    print("Greetings, I am 6, I am an AI assistant, what can I do for you?")
    talk("Greetings, I am 6, I am an AI assistant, what can I do for you?")

def who_created_assistant():
    print("I was created by Aniket.")
    talk("I was created by Aniket.") 
    print("I was created in VS Code using Python.") 
    talk("I was created in VS Code using Python.")
    
def about_the_creator():
    print("My creator name is Aniket and he is a B Tech CSE student and he is studying in HNB Garhwal University. His roll number is 21134501015.")
    talk("My creator name is Aniket and he is a B Tech CSE student and he is studying in HNB Garhwal University. His roll number is 21134501015.")

def questions():
    talk("Searching on Google...")
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    try:
        summary = wikipedia.summary(query, sentences=1)
        print(summary)
        talk(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous search query. Please refine your search.")
        talk("Ambiguous search query. Please refine your search.")
    except wikipedia.exceptions.PageError as e:
        print("No information found. Please try again.")
        talk("No information found. Please try again.")

def take_screenshot():
    talk("Tell me the name for the file")
    name = takeCommand().lower()
    time.sleep(3)
    img = py.screenshot()
    img.save(f"{name}.png")
    talk(f"Screenshot saved as {name}.png")

def adjust_volume(direction):
    if direction == "up":
        for _ in range(5):
            py.press('volumeup')
    elif direction == "down":
        for _ in range(5):
            py.press('volumedown')

def open_system_feature(feature_name):
    talk(f"Opening {feature_name}...")
    if feature_name == "spotlight":
        py.hotkey("alt", "space")
    elif feature_name == "task manager":
        py.hotkey("ctrl", "shift", "esc")
    elif feature_name == "file explorer":
        py.hotkey("win", "e")
    elif feature_name == "minimize all":
        py.hotkey("win", "m")
    elif feature_name == "restore minimized windows":
        py.hotkey("win", "shift", "m")

# Main Function
if __name__ == "__main__":
    engine = initialize_engine()
    create_db()
    wake_words = get_wake_words()
    is_awake = False
    current_user = None
    
    while True:
        if not is_awake:
            is_awake = respond_to_wake_words(wake_words)
            if is_awake:
                greet()
                current_user = ask_user_details()  # Ask for user details when assistant wakes up
                talk("I can now assist you with your queries.")
        else:
            query = takeCommand().lower()
            print("Assistant is awake and Listening")
            
            if "go to sleep" in query:
                print("Alright then, Saayonara...")
                talk("Alright then, saayonara...")
                is_awake = False
                current_user = None
                continue

            if "update details" in query:
                update_user_details()
                
            elif "retrieve details" in query:
                retrieve_user_details()

            elif "play" in query:
                play_on_youtube(query)
            elif "search" in query and "youtube" in query:
                search_on_youtube(query)
            elif "time" in query:
                get_time()
            elif "date" in query:
                get_today_date()
            elif "tell me about myself" in query:
                talk("What is your name?")
                name = takeCommand().lower()
                tell_current_user_details(name)
            elif "search" in query and "google" in query:
                query = query.replace("search google for", "")
                search_on_google(query)
            elif any(greet_word in query for greet_word in ["hi", "hello", "hey"]):
                response = respond_to_greetings(query)
                if response:
                    talk(response)
            elif "what can you do" in query:
                what_can_you_do()
            elif "how are you" in query:
                respond_to_how_are_you()
            elif "who are you" in query:
                introduce_assistant()
            elif "who created you" in query:
                who_created_assistant()
            elif "who is your creator" in query:
                about_the_creator()
            elif "question" in query or "tell me about" in query or "wikipedia" in query:
                questions()
            elif "screenshot" in query:
                take_screenshot()
            elif "volume up" in query:
                adjust_volume("up")
            elif "volume down" in query:
                adjust_volume("down")
            elif "open" in query and any(kw in query for kw in ["spotlight", "task manager", "file explorer", "minimize all", "restore minimized windows"]):
                feature_name = query.replace("open", "").strip()
                open_system_feature(feature_name)
            elif "go to sleep" in query:
                talk("Going to sleep now.")
                is_awake = False
