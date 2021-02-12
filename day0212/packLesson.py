import tkinter
root=tkinter.Tk()
root.geometry('300x200')

#ボタン作成
btn=tkinter.Button(root,text='開始',width=14)
#配置
btn.pack(fill='x',padx=20,side='left')
btn=tkinter.Button(root,text='終了',width=14)
btn.pack(fill='x',padx=20,side='left')

root.mainloop()

