import json
import os

# Check if file exists and is not empty
if not os.path.exists("users.json") or os.stat("users.json").st_size == 0:
    users = {}
else:
    with open("users.json", "r") as f:
        users = json.load(f)

# Input new user info
new_username = input("Enter new username: ")
new_password = input("Enter password: ")

# Add new user
if new_username in users:
    print("User already exists!")
else:
    users[new_username] = new_password
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)
    print(f"User {new_username} added successfully!")
