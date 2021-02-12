import tkinter

root=tkinter.Tk()
root.geometry('300x200')

la=tkinter.Label(root,text='Hello everyBody',bg='yellow',)
la.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
lb=tkinter.Label(root,text='Oh My God',bg='red',bd=2)
lb.grid(row=1,column=0,padx=5,pady=5)
lc=tkinter.Label(root,text='See you tomorrow',bg='LightSkyBlue',bd=2)
lc.grid(row=1,column=1,padx=5,pady=5)
