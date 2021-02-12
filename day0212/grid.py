import tkinter

root=tkinter.Tk()
root.geometry('300x200')

la=tkinter.Label(root,text='Hello everyBody',bg='yellow')
la.grid(row=0,column=0,colmnspan=2,padx=5,pady=5)

root.mainloop()
