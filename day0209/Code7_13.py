import requests
import codecs
response=requests.get('http://www.python.org/downloads/')
text=response.text

with codecs.open('index.html','w','utf-8')as file:
	file.write(text)
