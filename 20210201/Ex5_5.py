def int_input(msg):
	return int(input(msg+'を入力してください>>'))

def calc_payment(amount,people=2):
	





dnum=amount/people
pay=dnum//100*100

if dnum>pay:
	pay(pay+100)

payorg=amount-pay*(people-1)

print('***支払総額***')
print('一人当たり{}円,{}幹事は{}円です'.format(pay,people-1,payorg))
