import requests

r = requests.get('http://norvig.com/big.txt')
f = open('big.txt', 'w')
f.write(r.content)
