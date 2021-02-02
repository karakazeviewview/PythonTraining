setA={'カメラ','散歩','ゲーム','映画','料理'}
setB={'カメラ','散歩','ゲーム','映画','料理'}
input('心の準備ができたらenterキーを押してください')
result=(len(setA & setB)/len(setA | setB))*100
print('二人の相性は',result,'%です')
