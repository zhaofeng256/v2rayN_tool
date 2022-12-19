from urllib import parse
import requests
import pyperclip
import sys
url=sys.argv[1]
u = requests.get(url)
u = u.content.decode()
u = parse.unquote(u)
pre = '&url='
start=u.find(pre)+len(pre)
u = u[start:]
u = u.replace('|','\n')
print(u)
pyperclip.copy(u)
