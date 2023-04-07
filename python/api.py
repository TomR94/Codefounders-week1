print('start api read application')

import requests

paginaresult = requests.get('https://catfact.ninja/facts')
feitjes = paginaresult.json()

print(feitjes['current page'])
print(feitjes['data'][0])

