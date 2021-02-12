def sum_of4(n):#再帰処理、コールスタック
	if n<=1:
		return n
	else:
		return n*sum_of4(n-1)

num = input("正の整数を入力してください。")
ans=sum_of4(int(num))
print('1から',num,"までの積は", ans, "です。".strip())

