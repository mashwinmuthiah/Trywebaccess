import urllib.request

fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
for line in fhand:
    print(line.decode().strip())
