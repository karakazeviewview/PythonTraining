'''
print('サイコロを何回ふる？>>')
val=input()
print(val)
for diceroll in range(input):
names=['issiki','kawasaki','遠藤']
for name in names:
	print(name)
	'''
import random
num=int(input('サイコロを何回ふる?>>'))
dices=[random.randint(1,6) for _ in range(num)] #アンダーバーとは？
print(dices)
print('合計は',sum(dices),'でした')

