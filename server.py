import time
from datetime import datetime
from flask import Flask, request

#pyuic5 messanger.ui -o clientui.py

app = Flask(__name__)

messages = [
    {"username": "Jack", "text": "Hello", "time": time.time()},
    {"username": "Mary", "text": "Hi, Jack", "time": time.time()}
]

users = {
    # username : password
    "Jack": "black",
    "Mary": "12345"
}


@app.route("/")
def hello():
    return "Hello, my server!"


@app.route("/status")
def status():
    return {"status": True}


@app.route("/history")
def history():
    """
    requst: ?after=1234567890.4567
    response: {
    "messages": [{"username": username, "text": text, "time": time.time()},
    ...]
    }
    :return:
    """
    after = float(request.args["after"])

    filtered_messages = [message for message in messages if after < message["time"]]

    # filter_messages = []
    # for message in messages:
    #     if after < message["time"]:
    #         filter_messages.append(message)

    return {"messages": filtered_messages}


@app.route("/statistic")
def statistic():
    # Выводит статистику обо всех сообщениях и всех пользователях на сервере
    number_of_users = 0
    number_of_messages = 0
    users_in_mes = []

    for users_messages in messages:
        if users_messages["username"] not in users_in_mes:
            users_in_mes.append(users_messages["username"])
            number_of_users += 1
        number_of_messages += 1

    all_statistic = {"Users": number_of_users,
                     "All messages": number_of_messages}
    return all_statistic


@app.route("/userstat", methods=["POST"])
def userstat():
    data_name = request.json
    username = data_name["username"]
    user_number_mes = 0

    for message in messages:
        if username == message.get("username"):
            user_number_mes += 1

    return str(user_number_mes)


@app.route("/server_time")
def server_time():
    result = {
        "status": True, "time": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    return result


@app.route("/send", methods=["POST"])
def send():
    """
    requst: {"username": "str", "password": "str", "text": "str"}
    response: {"ok": true}
    :return:
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    text = data["text"]

    # если такой пользователь существует -> проверим пароль
    # иначе мы регистрирыем
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    messages.append({"username": username, "text": text, "time": time.time()})

    return {"ok": True}


app.run()
