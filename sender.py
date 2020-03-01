import requests

username = input("Enter username: ")
password = input("Enter password: ")

while True:
    text = input("Enter text: ")
    response = requests.post(
        "http://127.0.0.1:5000/send",
        json={"username": username, "password": password, "text": text}
    )
    if not response.json()["ok"]:
        print("Access denied")
