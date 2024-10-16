import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from textblob import TextBlob
from spellchecker import SpellChecker

# Create a themed window with a darker theme
root = ThemedTk(theme="equilux")
root.title("Spelling Checker")
root.geometry("600x450")
root.config(background="#2E2E2E")

def check_spelling():
    word = enter_text.get()
    
    # Check spelling with TextBlob
    corrected_word = str(TextBlob(word).correct())
    
    # Cross-verify with SpellChecker
    spell = SpellChecker()
    most_likely_words = list(spell.candidates(word))
    
    # Combine results
    result = f"Result 1: {corrected_word}\nResult 2: {', '.join(most_likely_words[:3])}"
    
    cs.config(text="Correct Spelling Is :")
    spell_label.config(text=result)

# Heading
heading = ttk.Label(root, text="Spelling Checker", font=("Trebuchet Ms", 30, "bold"), background="#2E2E2E", foreground="#FFFFFF")
heading.pack(pady=(30, 10))

# Frame for entry and button
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(pady=10)

# Entry widget
enter_text = ttk.Entry(input_frame, justify="center", font=("poppins", 23), foreground="#FFFFFF", background="#424242")
enter_text.grid(row=0, column=0, padx=5, pady=10)
enter_text.focus()

# Check button
check_button = ttk.Button(input_frame, text="Check", command=check_spelling)
check_button.grid(row=0, column=1, padx=5, pady=10)

# Labels for displaying results
cs = ttk.Label(root, font=("poppins", 18), background="#2E2E2E", foreground="#FFFFFF")
cs.pack(pady=(20, 5))

spell_label = ttk.Label(root, font=("poppins", 18), background="#2E2E2E", foreground="#FFFFFF")
spell_label.pack(pady=(5, 20))

root.mainloop()
