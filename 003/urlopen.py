import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://21ido.com/')
soup = BeautifulSoup(response, 'lxml')
titleArr = soup.select(".post-title-link")
for d in titleArr:
	print(d.string)
	
