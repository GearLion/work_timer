from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TEST_MIN = 1
CHECKMARK = "🗸"
REPS = 0
RUNNING = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(RUNNING)
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer.config(text="Long Rest")
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Short Rest")
    else:
        count_down(WORK_MIN * 60)
        timer.config(text="Work Timer")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = floor(count/60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
        global RUNNING
        RUNNING = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(REPS/2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkmarks.config(text=marks)
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=GREEN)

# Label
timer = Label()
timer.grid(column=1, row=0)
timer.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg="white", pady=10)

checkmarks = Label()
checkmarks.grid(column=1, row=3)
checkmarks.config(font=(FONT_NAME, 10, "bold"), bg=GREEN, fg=RED)

# Canvas with Tomato Image
canvas = Canvas(width=202, height=223, bg=GREEN, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato = PhotoImage(file="images/tomato.png")
canvas.create_image((101, 110), image=tomato)
timer_text = canvas.create_text((101, 130), text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")

# Buttons
start = Button(command=start_timer)
start.grid(column=0, row=2)
start.config(text="Start", font=(FONT_NAME, 10, "bold"), bg=RED, fg="white")

reset = Button(command=reset_timer)
reset.grid(column=2, row=2)
reset.config(text="Reset", font=(FONT_NAME, 10, "bold"), bg=RED, fg="white")

close = Button(command=window.destroy)
close.grid(column=3, row=0)
close.config(text="Close", font=(FONT_NAME, 8, "bold"), bg=RED, fg="white")

window.mainloop()
