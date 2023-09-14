import logging, websocket, sys
from websocket_server import WebsocketServer
from typing import TypedDict

class Client(TypedDict):
    id: str
    handler: object
    address: tuple[str, int]

def on_message(client:Client, server, message:str):
    pass

def on_connect(client:Client, server):
    pass

def on_disconnect(client:Client, server):
    pass
    
server = WebsocketServer(host='0.0.0.0', port=8765, loglevel=logging.INFO)
server.set_fn_message_received(on_message)
server.set_fn_new_client(on_connect)
server.set_fn_client_left(on_disconnect)
server.run_forever(threaded=True)

while True:
    try:
        message = input("Enter a message: ")
    except (KeyboardInterrupt, EOFError):
        break
