x=[n for n in range(1,8)]
print(x)
# [1, 2, 3, 4, 5, 6, 7]
x=[n**2 for n in range(1,8)]
print(x)
# [1, 4, 9, 16, 25, 36, 49]
x=[n for n in range(1,8) if n %2==0]
# [2, 4, 6]
print(x)
x=[n for n in range(8,15) if n %2==0]
print(x)
# [8, 10, 12, 14]
"""
x=list()
for n in range(1,8):
	if n % 2==0:
		x.append(n)
"""
x=[i*10+j for i in range(1,3) for j in range(2,5)]
"""
x=list()
for n in range(1,3):
	for j in range(2,5):
		x.append(i*10+j)
"""
print(x)
# [12, 13, 14, 22, 23, 24]

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)
# [[17, 18, 19], [27, 28, 29]]

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

matrix2=[]
for i in range(row):
	temp=[]
	for j in range(col):
		temp.append(1 if i==j else 0)
	matrix2.append(temp)
print(matrix2)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

x=[[i*10+j for j in range(10,19)] for i in range(5,9)]
print(x)
x=[[i*10+j for j in range(10,19)] for i in range(5,9)]
print(x)


x=[n for n in range(1,11)]
print(x)



x=[[i*10+j for j in range(1,11)]
print.print(data)
