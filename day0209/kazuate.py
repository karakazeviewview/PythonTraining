from random import randint
print('数当てゲームを始めます。３桁の数を当ててください！')
answer=list()
for n in range(3):
	answer.append(randint(0,9))
is_continue=True
while is_continue==True:
	prediction=list()
	for n in range(3):
		data=int(input('{}桁目の予想入力(0~9) >>'.format(n+1)))
		prediction.append(data)
	hit=0
	blow=0
	for n in range(3):
		if prediction[n]==answer[n]:
			hit+=1
		else:
			for m in range(3):
				if prediction[n]==answer[m] and n!=m:
print('{}ヒット！{}ボール！'.format(hit,blow))
if hit==3:
	print('正解です！')
	is_continue=False
else:
	if int(input())
