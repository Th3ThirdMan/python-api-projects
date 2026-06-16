import requests
import csv


response = requests.get("https://JsonPlaceholder.typicode.com/users")

users = response.json()
with open("user_exporter/users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Company", "Website"])
    
    for user in users:
            writer.writerow([
                user["name"], 
                user["email"], 
                user["company"]["name"],
                user["website"]
                ])
