import urllib.request
import datetime

response = urllib.request.urlopen('http://baidu.com')
print(response.headers["Date"])

'''
now = datetime.strptime(response.headers["Date"], "%Y-%m-%d %H:%M:%S")
print(now)
'''