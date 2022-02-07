"""The launcher of snake game."""

import tkinter as tk
import tkinter.messagebox as mb
import snake

DISPLAY_MIN = 200
SNAKE_MIN = 10


dw = 100
dh = 100
sw = 10

def btn_play_click():
    """
    The handler of btn_play click.

    NOTE
    ----
    The entered data (dw, dh, sw) must be digit.
    If data is not digits, this will couse an error.
    """

    def is_valid(dw, dh, sw):
        """
        Validation input data.

        Parameters
        ----------
        dw, dh, sw, ss : int
            The width, the height of display and the width, the speed of snake.

        Returns
        -------
        True, False : boolean
            Returns 'True' if input data is valid, else returns 'False'.
        """
        if (dw >= DISPLAY_MIN) and (dh >= DISPLAY_MIN ) and (sw >= SNAKE_MIN):
            if ((sw <= (dw//10)) or (sw <= (dh//10))):
                return True
            else:
                return False
        else:
            return False

    try:
        dw = int(display_width_entry.get())
        dh = int(display_height_entry.get())
        sw = int(snake_width_entry.get())
        ss = int(snake_speed_entry.get())
        if is_valid(dw, dh, sw):
            start_game(dw, dh, sw, ss)
        else:
            msg = "Check the entered data."
            mb.showerror("Error", msg)

    except ValueError:
        msg = "Check the entered data. It must be digits."
        mb.showerror("Error", msg)

def start_game(dw, dh, sw, ss):
    """
    Start the game.

    Parameters
    ----------
    dw, dh, sw, ss : int
        The width, the height of display and the width, the speed of snake.
    """

    snake.main(dw, dh, sw, ss)

"""Seting start window."""
start_window = tk.Tk()
start_window.title("launcher")

frame1 = tk.Frame(master = start_window,
                  bg = "black")

"""The label "Welcome to the "Snake" game!" """
welcome_lbl = tk.Label(master = frame1,
                       width = 27,
                       text = 'Welcome to the "Snake" game!',
                       bg = "black",
                       fg = "yellow")
welcome_lbl.pack()


"""Setting the input data."""
setting_frame= tk.Frame(master = start_window,
                        bg = "black")

"""The label "Display width" """
display_width_lbl = tk.Label(master = setting_frame,
                             width = 27,
                             text = "Display width (>=" + str(DISPLAY_MIN) +
                                     ")",
                             bg = "black",
                             fg = "yellow")
display_width_lbl.pack()

"""The text box which sets the display width"""
display_width_entry= tk.Entry(master = setting_frame)
display_width_entry.insert(0, "200")
display_width_entry.pack()

"""The label "Display height" """
display_height_lbl = tk.Label(master = setting_frame,
                              text = "Display height (>=" + str(DISPLAY_MIN) +
                                      ")",
                              bg = "black",
                              fg = "yellow")
display_height_lbl.pack()

"""The text box which sets the display height"""
display_height_entry= tk.Entry(master = setting_frame)
display_height_entry.insert(0, "200")
display_height_entry.pack()

"""The label "Snake width" """
snake_width_lbl = tk.Label(master = setting_frame,
                           text = "Snake width (>=" + str(SNAKE_MIN) + ")",
                           bg = "black",
                           fg = "yellow")
snake_width_lbl.pack()

"""The text box which sets snake width"""
snake_width_entry = tk.Entry(master = setting_frame)
snake_width_entry.insert(0, "20")
snake_width_entry.pack()





"""The label "Snake speed """
snake_speed_lbl = tk.Label(master = setting_frame,
                           text = "Snake speed",
                           bg = "black",
                           fg = "yellow")
snake_speed_lbl.pack()

"""The text box which sets snake speed"""
snake_speed_entry = tk.Entry(master = setting_frame)
snake_speed_entry.insert(0, "1")
snake_speed_entry.pack()


"""The button of start the game."""
play_btn = tk.Button(master = setting_frame,
                     text = "Play",
                     command = btn_play_click,
                     width = 24,
                     height = 3,
                     bg = "blue",
                     fg = "yellow")
play_btn.pack()
frame1.pack()
setting_frame.pack()
start_window.mainloop()
