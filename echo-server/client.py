import websocket, sys

ws = websocket.WebSocket()
ws.connect(f"ws://{sys.argv[1]}")

while True:
    try:
        message = input("Enter a message: ")
    except (KeyboardInterrupt, EOFError):
        ws.close()
        break
    ws.send(message)
    response = ws.recv()
    print("Received:", response)
