import json

ar = []

with open('cenz.txt', encoding='utf-16') as r:
    for i in r:
        n = i.lower().split(',')
        if n != '':
            ar.append(n)

with open('cenz.json', 'w', encoding='utf-16') as e:
    json.dump(ar, e)
