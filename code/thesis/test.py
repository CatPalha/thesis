from tkinter import Tk, messagebox


### MESSAGE BOX ####

tk = Tk()
#!!!Hide the main window!!!
tk.wm_withdraw()

teste_1 =  3
teste_2 = True

messagebox.showinfo("Midge info", "Generation number: "+ str(teste_1) + "\n Reproduction: " + str(teste_2))

# def popup():
#     #info var returns 'ok'
#     info = messagebox.showinfo("Midge info", "Generation number: "+ str(teste_1) + "\n Reproduction: " + str(teste_2))
#     #print(info)

#Button(tk, text = "PopUp", command = popup).pack()

#tk.mainloop()

#### INPUT ####

from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

root.mainloop()