import websocket, sys, threading

def on_message(client:websocket.WebSocketApp, message:str):
    print("\nReceived:", message)

def on_close(client:websocket.WebSocketApp, *_):
    pass

def on_open(client:websocket.WebSocketApp):
    pass

ws = websocket.WebSocketApp(f"ws://{sys.argv[1]}", on_message=on_message, on_close=on_close, on_open=on_open)
threading.Thread(target=ws.run_forever).start()

while True:
    try:
        message = input("Enter a message: ")
    except (KeyboardInterrupt, EOFError):
        ws.close()
        break
    ws.send(message)

    
