import turtle
ts=[]

def setup():
	global ts
	startline=-620
	screen=turtle.Screen()
	screen.setup(1290,720)

	t_y=[-40,-20,0,20,40]
	t_color=['blue','red','purple','brown','green']

	for i in range(len(t_y)):
		t=turtle.Turtle()
		t.shape('turtle')
		t.penup()
		t.setpos(startline,t_y[i])
		t.color(t_color[i])
		t.pendown()
		ts.append(t)

setup()
turtle.mainloop()
