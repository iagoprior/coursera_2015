import json
# list[ {dict}, {dict}]
data = '''[
       { "id" : "001",
         "x" : "2",
         "name" : "Chuck"
       } ,
       { "id" : "009",
         "x" : "7",
         "name" : "Ed"
       }
]'''

info = json.loads(data)
print(info)
print(len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attributes', item['x'])