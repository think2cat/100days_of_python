import urllib.request
from bs4 import BeautifulSoup
import time


for i in range(2):
	if i > 0:
		if i == 1:
			url = 'http://21ido.com'
		else:
			url = 'http://21ido.com/page/' + str(i) + '/'
		print("get url: " + url)
	
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response, 'lxml')
		imgArr = soup.select("img")
		for d in imgArr:
			urlimg = "http://21ido.com/" + d.get("src")
			print("download img:" + urlimg)
			content = urllib.request.urlopen(urlimg).read()
			path = "D:\\git\\100days_of_python\\006\\" + str(time.time()) + "." + d.get("src").split(".")[-1]
			urllib.request.urlretrieve(urlimg, path)
			
