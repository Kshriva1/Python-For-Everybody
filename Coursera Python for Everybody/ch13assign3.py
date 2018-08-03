import json
import urllib.request,urllib.parse,urllib.error


url = input('Enter the url-')
print('Retrieving:',url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved:',len(data),'characters')

try:
    info = json.loads(data)
except:
    info = None
total = 0
for items in info['comments']:
    num = items['count']
    inum = int(num)
    total = total + inum
print(total)
