import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pyttsx3

# Initialize the speech engine
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
    engine.setProperty('rate', 140)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level 0 to 1
except Exception as e:
    print(f"Error initializing speech engine: {e}")

def speak_now():
    try:
        engine.say(text_var.get())
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")

def set_voice(index):
    engine.setProperty('voice', voices[index].id)

def set_rate(rate):
    engine.setProperty('rate', int(rate))

def set_volume(volume):
    engine.setProperty('volume', float(volume))

# Create a themed window with a futuristic theme
root = ThemedTk(theme="plastik")
root.title("Text to Speech")
root.geometry("600x350")
root.configure(bg="#2C3E50")

text_var = tk.StringVar()

frame = ttk.LabelFrame(root, text="Text to Speech", padding="10 10 10 10", style="Futuristic.TLabelframe")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label = ttk.Label(frame, text="Text:", style="Futuristic.TLabel")
label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(frame, textvariable=text_var, width=40, style="Futuristic.TEntry")
entry.grid(row=0, column=1, padx=5, pady=5)

button = ttk.Button(frame, text="Speak", command=speak_now, style="Futuristic.TButton")
button.grid(row=0, column=2, padx=5, pady=5)

# Dropdown for voice selection
voice_label = ttk.Label(frame, text="Voice:", style="Futuristic.TLabel")
voice_label.grid(row=1, column=0, padx=5, pady=5)
voice_options = [voice.name for voice in voices]
voice_dropdown = ttk.Combobox(frame, values=voice_options, style="Futuristic.TCombobox")
voice_dropdown.current(1)
voice_dropdown.grid(row=1, column=1, padx=5, pady=5)
voice_dropdown.bind("<<ComboboxSelected>>", lambda event: set_voice(voice_dropdown.current()))

# Slider for speech rate
rate_label = ttk.Label(frame, text="Rate:", style="Futuristic.TLabel")
rate_label.grid(row=2, column=0, padx=5, pady=5)
rate_slider = ttk.Scale(frame, from_=50, to=300, orient='horizontal', command=set_rate)
rate_slider.set(140)
rate_slider.grid(row=2, column=1, padx=5, pady=5)

# Slider for volume
volume_label = ttk.Label(frame, text="Volume:", style="Futuristic.TLabel")
volume_label.grid(row=3, column=0, padx=5, pady=5)
volume_slider = ttk.Scale(frame, from_=0, to=1, orient='horizontal', command=set_volume)
volume_slider.set(1)
volume_slider.grid(row=3, column=1, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Add styles for a futuristic theme
style = ttk.Style()
style.theme_use('clam')
style.configure("Futuristic.TLabelframe", background="#34495E", foreground="#ECF0F1")
style.configure("Futuristic.TLabel", background="#34495E", foreground="#ECF0F1")
style.configure("Futuristic.TEntry", fieldbackground="#1ABC9C", background="#1ABC9C", foreground="#ECF0F1")
style.configure("Futuristic.TButton", background="#1ABC9C", foreground="#ECF0F1")
style.configure("Futuristic.TCombobox", fieldbackground="#1ABC9C", background="#1ABC9C", foreground="#ECF0F1")

# Run the application
root.mainloop()
