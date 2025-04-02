import subprocess
import sys
import platform
# from TTS.tts import speak

def open_app(app_name):
    system_platform = platform.system()

    try:
        if system_platform == "Windows":
            subprocess.run(["start", app_name], check=True, shell=True)
        elif system_platform == "Linux":
            subprocess.run([app_name], check=True)
        elif system_platform == "Darwin":  # MacOS
            subprocess.run(["open", "-a", app_name], check=True)
        else:
            print(f"Unsupported platform: {system_platform}")
            return False

        print(f"Successfully opened {app_name}")
        # speak(f"Successfully opened {app_name}")
        return True

    except FileNotFoundError:
        print(f"Application '{app_name}' not found.")
        # speak(f"Application '{app_name}' not found.")
    except subprocess.CalledProcessError:
        print(f"Failed to open '{app_name}'. Command returned a non-zero exit status.")
        # speak(f"Failed to open '{app_name}'.")
    except Exception as e:
        print(f"An error occurred while opening '{app_name}': {e}")

    return False

def main():
    user_input = input("Enter the names of applications to open (separated by space): ")
    if not user_input.strip():
        print("No applications entered. Exiting.")
        return

    app_names = user_input.split()
    for app in app_names:
        open_app(app)

if __name__ == "_main_":
    main()