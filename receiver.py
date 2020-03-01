from datetime import datetime
from time import sleep

import requests

# "messages": [
#     {"username": username, "text": text, "time": time.time()},
#     ...
# ]

last_message_time = 0


while True:
    response = requests.get(
        "http://127.0.0.1:5000/history",
        params={"after": last_message_time}
    )
    data = response.json()
    for message in data["messages"]:
        beuty_time = datetime.fromtimestamp(message["time"])
        beuty_time = beuty_time.strftime("%Y/%m/%d %H:%M:%S")
        print(beuty_time, message["username"])
        print(message["text"])
        print()
        last_message_time = message["time"]

    sleep(1)

