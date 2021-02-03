'''
import random

ans=random.randint(1,100)
max_count=5
print('1~100の数字の中から一つ選んだよ。')
print('その数字を',max_count,'回以内に当ててね。')

for i in range(1,max_count+1):
    print(i,'回目、いくつかな?')
    num=int(input())
    if num==ans:
        print('当たり!!')
        break
    elif i==max_count:
        pass
    elif num > ans:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
else:
    print('残念~正解は',ans,'でした。')
'''
		


import random

num=random.randint(1,100)
max_count=100
int LUCKY_NO=77
Random rand=new Random()
while True:
	count++
	int ans=rand.nextInt(1000)
	if(num==LUCKY_NO)
		break
print count'回目に出ました'
