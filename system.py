#Necessary packages
#from tkinter import Label, Entry
import tkinter as tk
import time
import numpy as np

#Declare necessary objects
app = tk.Tk()
app.title("Midge's Artificial Ecosystem")
app.geometry("800x800")
#app.resizable(0,0)


#Start button
# def ClickStart():
#     """To start to run the simulation"""
    

#Start button
# def ClickStop():
#     """To stop to run the simulation"""


b_1 = tk.Button(app, text = "Start") #command = ClickStart)
b_1.pack()

b_2 = tk.Button(app, text = "Stop") #command = ClickStop)
b_2.pack()

"""
### Possible way to do the inputs: GRID DOES NOT WORK WHEN USING PACK IN THE SAME CLASS###
lb_1 = Label(app, text = "Insert the parameters")
lb_2 = Label(app, text = "Population number")
lb_3 = Label(app, text = "Agents number")
lb_4 = Label(app, text = "Generation number")

et_lb_1 = Entry(app)
et_lb_2 = Entry(app)
et_lb_3 = Entry(app)
et_lb_4 = Entry(app)

lb_1.grid(column = 0, row = 0, columnspan = 5, pady = 5) # sticky = w, e, n, s
lb_2.grid(column = 0, row = 1,  sticky = "w")
lb_3.grid(column = 1, row = 1,  sticky = "w") 
lb_4.grid(column = 2, row = 1,  sticky = "w") 
et_lb_1.grid(column = 0, row = 2)
et_lb_2.grid(column = 0, row = 2)
et_lb_3.grid(column = 1, row = 2)
# et_lb_4.grid(column = 2, row = 2)

"""

c = tk.Canvas(app, height = 600, width = 500)
c.pack(side = tk.LEFT)

#To build the grid which will be the artificial ecosystem
def CreateGrid(line_distance, c_width, c_height):
    """Function that creates our gridWorld"""
    
    # vertical lines at an interval of "line_distance" pixel
    for x in range(0, c_width, line_distance):
        c.create_line(x, 0, x, c_height)

    # horizontal lines at an interval of "line_distance" pixel
    for y in range(1, c_height + 2,line_distance):
        c.create_line(0, y, c_width, y)

c.bind('<Configure>', CreateGrid(50, 600, 500))


app.mainloop()