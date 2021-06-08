from tkinter import Tk

root = Tk()

# screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# set window geometry
x = screen_width/2 - 800/2
y = screen_height/2 - 600/2
root.geometry("800x600+%d+%d" % (x, y))

# main frame


root.mainloop()
