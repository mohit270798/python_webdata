import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_123421.html').read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
count = 0
sum = 0
for tag in tags:
    value = tag.contents
    sum = sum+int(value[0])
    count =count+1
print('Count ',count)
print('Sum ',sum)
