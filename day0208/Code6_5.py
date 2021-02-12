class Hero:
	name='松田'
	hp=100
	def sleep(self,hours):
		print('{}は{}時間寝た！'.format(self.name,hours))
		self.hp=self.hp+hours
print('スッキリファンタジー')
h=Hero()
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))
