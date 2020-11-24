import json
data = '''

[
    {
    "name" : "Diego",
    "phone" : {
        "type" : "intl",
        "number" : "+59172698564"
        }      
    },
    
    {
    "name" : "Dylan",
    "phone" : {
        "type" : "intl",
        "number" : "++596285477"
        }      
    }
]
'''
#It return a python dictionary
info = json.loads(data)
print('User count:',len(info))

for user in info:

    print("Nombre:",user["name"])
    print("Numero:",user["phone"]["number"])




