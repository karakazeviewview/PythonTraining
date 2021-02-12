

class GameCharacter:
	def __init__(self,job,life,imgfile):
		self.job=job
		self.life=life


	def info(self):
		print(self.job)
		print(self.life)

warrior=GameCharacter('戦士',100)
##rint(warrior.job)
##print(warrior.life)
warrior.info()




'''
Pythonではclass名として
第一引数にself,他はフィールド。

pythonはnewがない。
インスタンス 名、ドットフィールド名

クラス内で定義されている関数をメソッドという

'''
