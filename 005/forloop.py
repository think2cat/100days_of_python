import urllib.request
from bs4 import BeautifulSoup

for i in range(5):
	if i > 0:
		if i == 1:
			url = 'http://21ido.com'
		else:
			url = 'http://21ido.com/page/' + str(i) + '/'
		print(url)
	
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response, 'lxml')
		titleArr = soup.select(".post-title-link")
		for d in titleArr:
			print(d.string)
