from random import randint
nums=3
ans=[randint(0,9) for i in range(nums)]
while True:
	hit=blow=0
	usr=[int(s) for s in input('カンマ区切りで入力>').split(',')]
	if len(usr)!=nums:
		print('正解は',ans,'です')
		break
	for i in range(len(usr)):
		for j in range(len(ans)):
			if usr[i]==ans[j]:
				if i==j:
					hit+=1
				else:
					blow+=1

	if hit==nums:
		print('正解')
		break
	else:
		print('{}hit {}blow'.format(hit,blow))

