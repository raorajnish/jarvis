import pyttsx3
import subprocess
import random
import sys


def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', 'pyttsx3'])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False
    return True

def speak(text, voice_id=0):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set voice based on default or provided voice ID
    voices = engine.getProperty('voices')
    try:
        engine.setProperty('voice', voices[voice_id].id)
    except IndexError:
        print(f"Invalid voice ID. Using default voice.")
        engine.setProperty('voice', voices[0].id)
    
    # Randomly vary the pitch
    pitch_variation = random.uniform(50, 200)  # Adjust the range as needed
    engine.setProperty('pitch', pitch_variation)
    
    # Set speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "_main_":
    if install_dependencies():
        user_text = input("Enter the text to convert to speech: ")
        speak(user_text)