import json

data = {"name":"a3","email":"win@","pass":"password123"}

myapi =json.dumps(data)
print(myapi)
print(type(myapi))
