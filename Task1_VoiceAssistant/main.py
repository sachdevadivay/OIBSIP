import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser


# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech and print it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the microphone and convert speech to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Sorry, I am having trouble connecting to the speech recognition service.")
        return ""


def process_command(command):

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # Date
    elif "date" in command or "today" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}.")

    # Web search
    elif "search" in command:
        search_query = command.replace("search", "").strip()

        if search_query:
            speak(f"Searching for {search_query}.")
            webbrowser.open(
                "https://www.google.com/search?q=" +
                search_query.replace(" ", "+")
            )
        else:
            speak("What would you like me to search for?")

    # Exit
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    # Unknown command
    else:
        speak("Sorry, I don't understand that command.")

    return True


def main():

    speak("Hello! I am your voice assistant. How can I help you?")

    running = True

    while running:
        command = listen()

        if command:
            running = process_command(command)


if __name__ == "__main__":
    main()
