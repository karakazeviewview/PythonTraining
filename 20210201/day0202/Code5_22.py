def eat(breakfast,lunch='ラーメン',dinner='カレー'):
	print('朝は{}を食べました'.format(breakfast))
	print('昼は{}を食べました'.format(lunch))
	print('夜は{}を食べました'.format(dinner))

eat('トースト','おにぎり')
eat('ばなな','そば','焼肉')

eat('トースト')
eat('トースト',dinner='焼きそば')
