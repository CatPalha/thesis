from tkinter import Tk, messagebox


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