import subprocess
import sys
import speech_recognition as sr

# Function to install a package using subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure the required package is installed
try:
    import speech_recognition as sr
except ImportError:
    install("speechrecognition")
    import speech_recognition as sr



# Function to recognize speech
def listen():
    r = sr.Recognizer()
    r.dynamic_energy_adjustment_damping = 0.3
    r.dynamic_energy_ratio = 0.9
    r.dynamic_energy_threshold = False
    r.pause_threshold = 0.5
    r.operation_timeout = None
    r.non_speaking_duration = 0.5
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing speech...")
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the speech recognition function
if __name__ == "_main_":
    listen()