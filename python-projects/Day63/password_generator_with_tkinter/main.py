from tkinter import *

# --------------------------PASSWORD GENERATOR ------------------------

# ------------------------ SAVE PASSWORD -----------------------


# ------------------------ UI SETUP -----------------------------------

window = Tk()
window.title("Password Generator")
window.config(padx=2, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
window.mainloop()
