import tkinter as tk
from datetime import date
def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        birth_date = date(year, month, day)
        age = today.year-birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        result_label.config(
            text=f"Hey {name}!\nYou are {age} years old.",
            fg="#80C5A3"
        )
    except ValueError:
        result_label.config(
            text="Please enter valid details.",
            fg="red"
        )

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#B9D9E5")

# Frame for input fields
frame = tk.Frame(root, bg="#DCAFAF")
frame.pack(pady=20)

# Name
tk.Label(frame, text="Name:", bg="#DFB3B3").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, pady=5)

# Day
tk.Label(frame, text="Day:", bg="#D6A9A9").grid(row=1, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(frame)
day_entry.grid(row=1, column=1, pady=5)

# Month
tk.Label(frame, text="Month:", bg="#DEA9A9").grid(row=2, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(frame)
month_entry.grid(row=2, column=1, pady=5)

# Year
tk.Label(frame, text="Year:", bg="#E1B2B2").grid(row=3, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1, pady=5)

# Button
calc_button = tk.Button(
    root,
    text="Calculate Age",
    command=calculate_age,
    bg="#242F6D",
    fg="white",
    width=15
)
calc_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    bg="#5E2323",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=10)

# Run the application
root.mainloop()