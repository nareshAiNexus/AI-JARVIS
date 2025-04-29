import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import tkinter as tk
from tkinter import scrolledtext, messagebox
from threading import Thread
import subprocess

# Initialize engine and recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()

# Setup engine properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice
engine.setProperty('rate', 150)

# Colors and fonts
BG_COLOR = "#1E1E1E"
FG_COLOR = "#00FFAB"
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_STATUS = ("Consolas", 14)

# 🔊 Speak and display message
def talk(text):
    update_chat("🤖 Jarvis", text)
    engine.say(text)
    engine.runAndWait()

# 🧠 LLaMA3 call
def llama3_generate_response(command):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", command],
            capture_output=True, text=True, check=True
        )
        response = result.stdout.strip()
        return response if response else "Sorry, I couldn't generate a response."
    except subprocess.CalledProcessError as e:
        print(f"Error calling Ollama: {e}")
        print("stderr:", e.stderr)
        return "Sorry, I couldn't reach the model right now."

# 💬 Process voice command
def respond(command):
    update_chat("🧑 You", command)

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time_now}')
    elif 'goodbye' in command or 'exit' in command:
        talk('Goodbye, see you soon!')
        window.destroy()
        exit()
    else:
        response = llama3_generate_response(command)
        talk(response)

# 🎤 Start microphone listener
def listen():
    while True:
        try:
            with sr.Microphone() as source:
                status_label.config(text="🎙️ Listening...")
                window.update()
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                respond(command)
        except Exception as e:
            print('Error:', e)
            continue

# 📋 Right-click copy
def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Copied", "Message copied to clipboard!")

def on_right_click(event):
    try:
        selected_text = chat_log.get(tk.SEL_FIRST, tk.SEL_LAST)
        copy_to_clipboard(selected_text)
    except:
        pass

# 🪟 GUI setup
window = tk.Tk()
window.title("🤖 Jarvis AI Assistant")
window.geometry("700x500+100+100")
window.configure(bg=BG_COLOR)

header = tk.Label(window, text="🤖 JARVIS", fg="#00E0FF", bg=BG_COLOR, font=FONT_TITLE)
header.pack(pady=(10, 5))

# 💬 Scrollable chat window
chat_log = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg="#222222", fg=FG_COLOR,
                                     font=FONT_STATUS, width=80, height=20, bd=0, relief=tk.FLAT)
chat_log.pack(padx=20, pady=10)
chat_log.bind("<Button-3>", on_right_click)
chat_log.config(state=tk.DISABLED)

# 🔁 Chat updater
def update_chat(speaker, message):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"{speaker}: {message}\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

# 📢 Bottom status label
status_label = tk.Label(window, text="🔄 Initializing Jarvis...", fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 12))
status_label.pack(pady=5)

# 🧵 Start listener thread
thread = Thread(target=listen)
thread.start()

window.mainloop()
