import tkinter as tk
import snake

def start_game():
    snake.main()

"""Seting start window"""
start_window = tk.Tk()

"""Welcome"""
frame1 = tk.Frame(master = start_window,
                  bg = "black")

welcome_lbl = tk.Label(master = frame1,
                       width = 27,
                       text = 'Welcome to the "Snake" game!',
                       bg = "black",
                       fg = "yellow")
welcome_lbl.pack()

"""Setting the input data"""
setting_frame= tk.Frame(master = start_window,
                        bg = "black")

display_width_lbl = tk.Label(master = setting_frame,
                             width = 27,
                             text = "Display width",
                             bg = "black",
                             fg = "yellow")
display_width_lbl.pack()

display_width_entry= tk.Entry(master = setting_frame)
display_width_entry.insert(0, "200")
display_width_entry.pack()

display_height_lbl = tk.Label(master = setting_frame,
                              text = "Display height",
                              bg = "black",
                              fg = "yellow")
display_height_lbl.pack()

display_height_entry= tk.Entry(master = setting_frame)
display_height_entry.insert(0, "200")
display_height_entry.pack()

snake_width_lbl = tk.Label(master = setting_frame,
                           text = "Snake width",
                           bg = "black",
                           fg = "yellow")
snake_width_lbl.pack()

snake_width_entry = tk.Entry(master = setting_frame)
snake_width_entry.insert(0, "20")
snake_width_entry.pack()


"""Start the game"""
play_btn = tk.Button(master = setting_frame,
                     text = "Play",
                     command = start_game,
                     width = 24,
                     height = 3,
                     bg = "blue",
                     fg = "yellow")
play_btn.pack()

frame1.pack()
setting_frame.pack()
start_window.mainloop()
