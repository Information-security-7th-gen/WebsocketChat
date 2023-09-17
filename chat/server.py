import logging, websocket, sys
from websocket_server import WebsocketServer, API as Server
from typing import TypedDict

class Client(TypedDict):
    id: str
    handler: object
    address: tuple[str, int]

def on_message(client:Client, server:Server, message:str):
    file=open(client["id"], "+w")
    print(message, file=file)
    file.close()
    print("\nReceived message:", message)

def on_connect(client:Client, server:Server):
    pass

def on_disconnect(client:Client, server:Server):
    pass
server = WebsocketServer(host='0.0.0.0', port=8765, loglevel=logging.INFO)
server.set_fn_message_received(on_message)
server.set_fn_new_client(on_connect)
server.set_fn_client_left(on_disconnect)
server.run_forever(threaded=True)

file=open("my_message", "w+")

while True:
    try:
        message = input("Enter a message: ")
        print(message, file=file)
        server.send_message_to_all(message)
    except (KeyboardInterrupt, EOFError):
        file.close()
        break
# wget http://192.168.1.30:8000/chat/server_log.py
# python3 server_log.py

# python3 client_log.py 192.168.0.{番号}:8765