def sum_of(n):
	sum=0
	for i in range(n+1):
		sum+=i
	return sum

def sum_of2(n):
	return sum(range(1,n+1))

def sum_of3(n):
	ls=[i for i in range(1,n+1)]
	return(sum(ls))

def sum_of4(n):#再帰処理、コールスタック
	if n<=1:
		return n
	else:
		return n+sum_of4(n-1)

num = input("正の整数を入力してください。")
ans=sum_of4(int(num))
print("までの和は", ans, "です。")
