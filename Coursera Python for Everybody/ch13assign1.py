import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data.decode())

results = tree.findall('.//comment')
print('Count:',len(results))
total = 0
for item in results:
    num = item.find('count').text
    inum = int(num)
    total = total + inum
print(total)
