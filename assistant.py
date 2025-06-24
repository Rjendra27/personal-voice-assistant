import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import threading
import time as time_module

# Global chat memory
chat_history = []

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print("🎙️ GIRI:", text)
    chat_history.append({"giri": text})
    with open("chat_memory.txt", "a") as f:
        f.write(f"GIRI: {text}\n")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        try:
            voice = listener.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            talk("I didn’t hear anything. Try again.")
            return ""
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
        chat_history.append({"you": command})
        with open("chat_memory.txt", "a") as f:
            f.write(f"You: {command}\n")
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def set_reminder():
    try:
        talk("What should I remind you about?")
        reminder_text = take_command()
        if not reminder_text:
            talk("Reminder not set. I didn't hear the task.")
            return

        talk("In how many minutes should I remind you?")
        time_text = take_command()
        if not time_text:
            talk("Reminder not set. I didn't hear the time.")
            return

        minutes = int(''.join(filter(str.isdigit, time_text)))
        seconds = minutes * 60

        def reminder_thread():
            time_module.sleep(seconds)
            talk(f"⏰ Reminder: {reminder_text}")

        thread = threading.Thread(target=reminder_thread)
        thread.start()

        talk(f"Reminder set for {minutes} minutes from now.")
    except:
        talk("Sorry, I couldn’t set the reminder.")

def comfort_loneliness():
    talk("I'm here with you, buddy. You're never really alone.")
    talk("Would you like me to tell a joke or play a song for you?")
    response = take_command()
    if "joke" in response:
        talk(pyjokes.get_joke())
    elif "song" in response or "play" in response:
        talk("What song would you like to hear?")
        song = take_command()
        if song:
            talk("Playing it on YouTube 🎵")
            pywhatkit.playonyt(song)
    else:
        talk("Okay, just know I'm always here for you 💖")

def run_assistant():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        talk("Opening Chrome 🚀")
        os.system("open -a 'Google Chrome'")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("open -a 'Visual Studio Code'")

    elif "remind me" in command or "set reminder" in command:
        set_reminder()

    elif "i feel lonely" in command or "i'm feeling lonely" in command or "i am lonely" in command:
        comfort_loneliness()

    elif "what did i say earlier" in command or "remember what i said" in command:
        recent = [msg["you"] for msg in chat_history if "you" in msg][-3:]
        if recent:
            talk("Here's what you said recently:")
            for line in recent:
                talk(line)
        else:
            talk("I don’t remember you saying anything yet.")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif command != "":
        talk("Sorry, I didn't understand that.")

if __name__ == "__main__":
    talk("Hello! I am Rajendra's personal assistant")
    while True:
        run_assistant()
