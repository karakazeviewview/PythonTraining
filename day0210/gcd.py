def gcd(x,y):#再帰処理、コールスタック
	if x%y==0:
		return y
	else:
		return x%(y-x)
			


x = input("正の整数を入力してください>>")
y = input("正の整数を入力してください>>")
#ans=int(gcd)
print("最大公約数は", ans, "です。".strip())

