name=list()
print('変更前のid: {}'.format(id(names)))
names.append('松田')
print('変更後のid: {}'.format(id(names)))

name='松田'
print('変更前のid: {}'.format(id(names)))
name='スーパー'+name
print('変更後のid: {}'.format(id(names)))

