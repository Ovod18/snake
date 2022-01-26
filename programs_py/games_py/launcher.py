import tkinter as tk
import snake

window = tk.Tk()
label_1 = tk.Label(text = "Hello, World!")
label_1.pack()

def start_game():
    snake.main()

button = tk.Button(window, text = "Start", command = start_game,
                               width = 25, height = 5,
                               bg = "blue", fg = "yellow")
button.pack()
window.mainloop()
