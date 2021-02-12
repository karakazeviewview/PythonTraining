def add_suffix(names):
	for i in range(len(names)):
		names[i]=names[i]+'さん'
	return names
before_names=['松田','浅木','工藤']
"""
copied_name=list()
for n in before_names:
	copied_name.append(n)
"""
#copied_name=before_names[:]
copied_name=before_names.copy()
after_names=add_suffix(copied_name)
print('さん付後:'+after_names[0])
print('さん付前:'+before_names[0])
