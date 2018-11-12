import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
