'''
import random
n1=random.randrange(10,50,2) # 10-50の範囲の偶数
n2=random.randrange(10,100,7) # 10-100の範囲の7の倍数
print(n1)
print(n2)
'''

import random
num=int(input('100~1000の範囲の偶数を幾つ生成する?>>'))
data=[random.randrange(100,1000,2) for _ in range(num)]
data.sort(reverse=True)
print(num,'個生成しました！降順に表示します',data)
