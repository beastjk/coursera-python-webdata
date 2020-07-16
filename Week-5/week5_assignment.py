import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_775997.xml')
text = ''''''
for line in fhand:
    text += line.decode()

print(text)

tree = ET.fromstring(text)

comment_counts = tree.findall('.//comment')
counts = tree.findall('.//count')
print('comment count: ', len(comment_counts))

cnt = 0
for num in counts:
    cnt += int(num.text)

print('Total sum of numbers: ', cnt)
