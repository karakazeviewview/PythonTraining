def add_suffix(name):
	name=name+'さん'
	return name
before_name='松田'
after_name=add_suffix(before_name)
print('さん付後:'+after_name[0])
print('さん付前:'+before_name[0])

