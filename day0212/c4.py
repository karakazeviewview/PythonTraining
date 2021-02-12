import tkinter

FNT=('Times New Roman',30)

class GameCharacter:
	def __init__(self,job,life,imgfile):
		self.job=job
		self.life=life
		self.img=tkinter.PhotoImage(file=imgfile)

	def draw(self,x,y):
		canvas.create_image(200,280,image=self.img)
		canvas.create_text(300,400,text=self.job,font=FNT,fill='red')
		canvas.create_text(300,480,text=self.life,font=FNT,fill='blue')

root=tkinter.Tk()
root.title('Class Lesson')
canvas=tkinter.Canvas(root,width=400,height=560,bg='white')
canvas.pack()

#character=GameCharacter('剣士',200,'swordsman.png')
character=[
	GameCharacter('戦士',200,'swordsman.png'),
	GameCharacter('忍者',160,'ninja.png')
]
character[0].draw(0,0)
character[1].draw(400,0)
root.mainloop()