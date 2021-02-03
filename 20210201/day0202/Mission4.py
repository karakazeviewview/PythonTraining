height=int(input('何段の階段を作る?>'))
for i in range(height):
	print(i)
	for j in range(i+1):
		print('*',end='')
	print()
