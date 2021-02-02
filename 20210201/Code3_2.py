name=input('あなたの名前を教えてください>>')
print('{}さんこんにちは'.format(name))
food=input('{}さんの好きな食べ物を教えてください>>'.format(name))

if food=='カレー': #Javaなら.equals
	print('素敵です。カレーは最高ですよね！')
else:
	print('私も{}が好きですよ'.format(food))
