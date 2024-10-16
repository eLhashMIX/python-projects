import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
import json

# Simulating online data fetching with a sample JSON
perfumes = {
    "Spring": [
        "Daisy by Marc Jacobs",
        "Light Blue by Dolce & Gabbana",
        "Blossom by Jimmy Choo",
        "Chanel Chance Eau Tendre"
    ],
    "Summer": [
        "Aqua di Gioia by Giorgio Armani",
        "Cool Water by Davidoff",
        "Sun di Gioia by Giorgio Armani",
        "Nautica Voyage"
    ],
    "Fall": [
        "Hypnotic Poison by Dior",
        "Tom Ford Tobacco Vanille",
        "Yves Saint Laurent Black Opium",
        "Marc Jacobs Decadence"
    ],
    "Winter": [
        "Burberry Brit",
        "Viktor & Rolf Flowerbomb",
        "Jo Malone Wood Sage & Sea Salt",
        "Giorgio Armani Si"
    ]
}

def suggest_perfume():
    season = season_var.get()
    suggestions = perfumes.get(season, ["No suggestions available"])
    suggestions_text = "\n".join(suggestions[:5])  # Limiting to top 5 suggestions
    result_label.config(text=f"Suggested perfumes for {season}:\n{suggestions_text}")

# Create a themed window with a futuristic theme
root = ThemedTk(theme="breeze")
root.title("Seasonal Perfume Recommender")
root.geometry("600x400")
style = ThemedStyle(root)
style.set_theme("breeze")

# Frame for main content
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Heading
heading = ttk.Label(frame, text="Seasonal Perfume Recommender", font=("Helvetica", 18, "bold"))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Dropdown to select season
season_var = tk.StringVar()
season_label = ttk.Label(frame, text="Select Season:")
season_label.grid(row=1, column=0, pady=5, sticky="e")
season_dropdown = ttk.Combobox(frame, textvariable=season_var, values=list(perfumes.keys()), state="readonly")
season_dropdown.grid(row=1, column=1, pady=5, sticky="w")

# Button to get suggestions
suggest_button = ttk.Button(frame, text="Get Suggestions", command=suggest_perfume)
suggest_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the results
result_label = ttk.Label(frame, text="", font=("Helvetica", 12), background="#e6e6e6", relief="solid", padding="10")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Make the app responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Run the application
root.mainloop()
