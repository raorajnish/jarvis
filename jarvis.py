from STT.stt import listen
from TTS.tts import speak
from Open_App.openapp import open_app
from Web_Open.web_open import open_Web
from Brain.Brain import Main_Brain

def main():
    print("Jarvis script started.")
    while True:
        try:
            text = listen().lower()
            # print(f"Received command: {text}")

            if "jarvis" in text:
                print("Calling Main_Brain...")
                response = Main_Brain(text)
                print(response)
                speak(response)
            elif "open" in text:
                if "website" in text:
                    speak("Opening website...")
                    text = text.replace("open", "").replace("website", "").strip()
                    open_Web(text)
                elif "app" in text:
                    print("Opening app...")
                    text = text.replace("open", "").replace("app", "").strip()
                    open_app(text)
            elif "bye" in text or "good bye" in text:
                response = Main_Brain(text)
                speak(response)
                break
            else:
                # print("Calling Main_Brain...")
                # response = Main_Brain(text)
                # speak(response)
                print("No valid command found.")
                speak("I didn't understand that command Can you repeat please?")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("I didn't understand that command")

if __name__ == "__main__":
    main()