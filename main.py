from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles To Kilometers!")
window.minsize(width=500, height=300)
window.config(padx=100, pady=60)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(pady=20, padx=20)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)
equals_label.config(pady=20, padx=20)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)
answer_label.config(pady=20, padx=20)

kilometers_label = Label(text="km")
kilometers_label.grid(column=2, row=1)
kilometers_label.config(pady=20, padx=20)

# Button
def button_clicked():
    miles = float(input.get())
    miles *= 1.609
    answer_label.config(text=miles)


# calls button_clicked() when pressed
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(pady=20, padx=20)


# Entry (Text box)
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
