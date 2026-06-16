import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

with open("users.txt", "w") as file:
    for user in data:
        file.write(user["name"] + " - " + user["email"] + "\n")

for user in data:
    print(user["name"], "-", user["email"])