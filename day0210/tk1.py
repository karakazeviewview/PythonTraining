import tkinter as tk
def bt_click():
	btn['text']='Clicked!'
root=tk.Tk()
root.title('My Window') #windowタイトルを設定
root.geometry('600x400') #windowの大きさを設定
#文字出力のためのラベルを作成
#ボタンを作成
btn=tk.Button(root,text='Hello World!',font=('Arial',50),command=bt_click) #fontはタプル
#labelを配置
btn.place(x=100,y=100)
root.mainloop()
