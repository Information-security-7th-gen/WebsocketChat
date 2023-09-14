import logging
from websocket_server import WebsocketServer

def on_message(client, server, message):
    server.send_message(client, message)
    
server = WebsocketServer(host='0.0.0.0', port=8765, loglevel=logging.INFO)
server.set_fn_message_received(on_message)
server.run_forever()