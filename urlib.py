import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fh = open('image1.jpg','wb')
fh.write(fhand)
fh.close()
