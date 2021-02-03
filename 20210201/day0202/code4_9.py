ages=[26,50,8,'ひみつ',20,78,25,22,'無回答',10,27,33]
num=5
samples=list()
for age in ages:
#第1匹数が第２引数の
	if not isinstance(age,int):
		continue
	if 20<=age<30:
		samples.append(age):
		if len(samples)==num:
			break
print(samples)
