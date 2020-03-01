from pprint import pprint

import requests

response = requests.get("http://127.0.0.1:5000/server_time")
pprint(response.json())

response = requests.post("http://127.0.0.1:5000/send",
                         json={"username": "Nick", "text": "Hello"})
pprint(response.json())

response = requests.get("http://127.0.0.1:5000/history")
pprint(response.json())