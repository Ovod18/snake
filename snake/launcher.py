"""This is the launcher for snake game.

    :platform: Linux
    :author: Ovod18

    |
"""

import tkinter as tk
import tkinter.messagebox as mb
import snake

DISPLAY_MIN = 200
"""The minimum display width, display height.

    :type: int
    :value: 200

    |
"""

SNAKE_MIN = 10
"""The minimum snake width.

    :type: int
    :value: 10

    |
"""

d_size = [200, 200]
"""The display size.

    :type: list[int, int]
    :value: 200,200

    |
"""

def is_valid(dw, dh, sw):
    """Validation input data.

    :param int dw: The display width
    :param int dh: The display height
    :param int sw: The snake width
    :returns: True or False
    :rtype: boolean

    |
    """

    if (d_size[0]>=DISPLAY_MIN) and (d_size[1]>=DISPLAY_MIN) and (sw>=SNAKE_MIN):
        if ((sw <= (d_size[0]//10)) or (sw <= (d_size[1]//10))):
            return True
        else:
            return False
    else:
        return False

def btn_play_click():
    """The handler of btn_play click.

    |
    """

    try:
        d_size[0] = int(display_width_entry.get())
        d_size[1] = int(display_height_entry.get())
        sw = int(snake_width_entry.get())
        ss = int(snake_speed_entry.get())
        if is_valid(d_size[0], d_size[1], sw):
            start_game(d_size[0], d_size[1], sw, ss)
        else:
            msg = "Check the entered data."
            mb.showerror("Error", msg)

    except ValueError:
        msg = "Check the entered data. It must be digits."
        mb.showerror("Error", msg)

def start(event):
    """Start :py:func:`.btn_play_click` with some event.

    :param object event: some event

    |
    """

    btn_play_click()

def start_game(dw, dh, sw, ss):
    """Start the game with following parameters.

    :param int dw: display width
    :param int dh: display height
    :param int sw: snake width
    :param int ss: snake width

    |
    """

    snake.main(d_size[0], d_size[1], sw, ss)

# Seting start window.
start_window = tk.Tk()
start_window.title("launcher")

# Start 'btn_play_click' with some event'
start_window.bind("<Return>", start)

frame1 = tk.Frame(master = start_window,
                  bg = "black")
frame1.pack()

# The label "Welcome to the "Snake" game!".
welcome_lbl = tk.Label(master = frame1,
                       width = 27,
                       text = 'Welcome to the "Snake" game!',
                       bg = "black",
                       fg = "yellow")
welcome_lbl.pack()

# Setting the input data.
setting_frame= tk.Frame(master = start_window,
                        bg = "black")
setting_frame.pack()

# The label "Display width".
display_width_lbl = tk.Label(master = setting_frame,
                             width = 27,
                             text = "Display width (>="+str(DISPLAY_MIN) +
                                     ")",
                             bg = "black",
                             fg = "yellow")
display_width_lbl.pack()

# The text box which sets the display width.
display_width_entry= tk.Entry(master = setting_frame)
display_width_entry.insert(0, "200")
display_width_entry.pack()

# The label "Display height".
display_height_lbl = tk.Label(master = setting_frame,
                              text = "Display height (>="+str(DISPLAY_MIN)+
                                      ")",
                              bg = "black",
                              fg = "yellow")
display_height_lbl.pack()

# The text box which sets the display height.
display_height_entry= tk.Entry(master = setting_frame)
display_height_entry.insert(0, "200")
display_height_entry.pack()

# The label "Snake width"
snake_width_lbl = tk.Label(master = setting_frame,
                           text = "Snake width (>=" + str(SNAKE_MIN) + ")",
                           bg = "black",
                           fg = "yellow")
snake_width_lbl.pack()

# The text box which sets snake width
snake_width_entry = tk.Entry(master = setting_frame)
snake_width_entry.insert(0, "20")
snake_width_entry.pack()

# The label "Snake speed 
snake_speed_lbl = tk.Label(master = setting_frame,
                           text = "Snake speed",
                           bg = "black",
                           fg = "yellow")
snake_speed_lbl.pack()

# The text box which sets snake speed
snake_speed_entry = tk.Entry(master = setting_frame)
snake_speed_entry.insert(0, "1")
snake_speed_entry.pack()


# The button of start the game.
play_btn = tk.Button(master = setting_frame,
                     text = "Play",
                     command = btn_play_click,
                     width = 24,
                     height = 3,
                     bg = "blue",
                     fg = "yellow")
play_btn.pack()

def main():
    """The main function in launcher.py

    |
    """

    start_window.mainloop()

if __name__ == "__main__":
    main()
