import os

from chat_app_project.settings import BASE_DIR

print(BASE_DIR)

file_path = os.path.join(BASE_DIR, '', 'secret.txt')

with open(file_path, 'r') as file:
    credentials = file.readlines()

# Extract the username and password from the contents
username = credentials[0].strip()
password = credentials[1].strip()

print(username)
print(password)