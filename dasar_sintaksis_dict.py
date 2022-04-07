users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite":   "Suite 879",
        "city":	"Wisokyburgh",
        "zipcode":	"90566-7771",
        "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print('\nUbah dict ke json')
import json
result = json.dumps(users)
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)
