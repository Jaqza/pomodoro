from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def clock_reset():
    global reps
    # reps = 9
    # canvas(counter_text)
    # canvas.itemconfig(counter_text, text = "00:00")
    # start_button.configure(state="active")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def clock_start():
    start_button.configure(state="disabled")
    global reps
    reps += 1
    if reps % 9 == 0:
        start_button.configure(state="active")
        return
    if reps % 8 == 0:
        check_marks["text"] += "✔"
        work_break.configure(text="Break",fg=PINK)
        count_down(10)
    elif reps % 2 == 1:
        work_break.configure(text="Work", fg=RED)
        count_down(4)
    elif reps % 2 == 0:
        work_break.configure(text="Break", fg=YELLOW)
        check_marks["text"] +="✔"
        count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    second = count % 60
    if second < 10:
        second = f"0{second}"
    if count >= 0:
        canvas.itemconfig(counter_text, text=f"{minutes}:{second}")
    window.after(1000, count_down, count - 1)
    if count == 0:
        clock_start()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.configure(padx=20,pady=20,relief="raised",borderwidth=20,background=GREEN)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=225)
canvas.configure(background=GREEN,highlightthickness=0)
canvas.create_image(100,112, image=image)
counter_text = canvas.create_text(100,130,text ="00:00",font=("Courier",30,"normal"),fill="white")
canvas.grid(column=1, row=1)

work_break = Label()
work_break.configure(text = "Timer",font=("Courier",37,"normal"),background=GREEN,justify="center",fg="white")
work_break.grid(column=1, row=0)

start_button = Button()
start_button.configure(text="start",relief="raised",borderwidth=7,background=GREEN,
                       activebackground=GREEN,command=clock_start)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.configure(text="Reset",relief="raised",borderwidth=7,background=GREEN,
                       activebackground=GREEN,command=clock_reset)
reset_button.grid(column=2, row=2)

check_marks = Label()
check_marks.configure(text="",background=GREEN,fg=RED)
check_marks.grid(column=1, row=3)

window.mainloop()