data=list() #listコンストラクタ 空っぽ
for i in range(10): #もうひとつ空っぽのlist
	  
	temp=list()
	for j in range(10):
		temp.append(0)
	data.append(temp)
print(data)
