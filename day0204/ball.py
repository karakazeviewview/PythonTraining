import random
GAME_COUNT=5
balls=list(range(1,100))
random.shuffle(balls)
awin=bwin=0
for i in range(GAME_COUNT):
	print(f'{i+1}回戦')
	a,b=balls.pop(),balls
	
