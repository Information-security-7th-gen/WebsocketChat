import logging
from websocket_server import WebsocketServer

def on_message(client, server, message):
    print("Received:", message)
    
server = WebsocketServer(host='0.0.0.0', port=8765, loglevel=logging.INFO)
server.set_fn_message_received(on_message)
server.run_forever(threaded=True)

while True:
    try:
        message = input("Enter a message: ")
    except (KeyboardInterrupt, EOFError):
        break
    server.send_message_to_all(message)

# http://192.168.1.30:8000/chat