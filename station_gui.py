import tkinter as tk

BUTTON_BACKGROUND_COLOR = "#115293"
BUTTON_FOREGROUND_COLOR = "#fefefe"
WINDOW_BACKGROUND_COLOR = "#0a0a0a"


def start():
    row = 0

    root = tk.Tk()
    root.geometry('600x300')

    # Heading Text
    text_widget = tk.Text(root, height=10, width=60)
    current_text = tk.Label(root, text="RFID Station")
    current_text.grid(column=1, row=row)
    row += 1

    # Current Text
    text_widget = tk.Text(root, height=10, width=60)
    current_text = tk.Label(root, text="")
    current_text.grid(column=1, row=row)
    row += 1

    # Current RFID Text
    text_widget = tk.Text(root, height=10, width=60)
    status_text = tk.Label(root, text="")
    status_text.grid(column=1, row=row)
    row += 1

    # Read Button
    read_text = tk.StringVar()
    read_btn = tk.Button(root, command=lambda: Sensor.read(current_text), textvariable=read_text,
                         bg=BUTTON_BACKGROUND_COLOR,
                         fg=BUTTON_FOREGROUND_COLOR)
    read_text.set("Read")
    read_btn.grid(column=1, row=row)
    row += 1

    # Write Button
    write_text = tk.StringVar()
    write_btn = tk.Button(root, command=lambda: Sensor.write(status_text), textvariable=write_text,
                          bg=BUTTON_BACKGROUND_COLOR,
                          fg=BUTTON_FOREGROUND_COLOR)
    write_text.set("Write")
    write_btn.grid(column=1, row=row)
    row += 1

    root.mainloop()
