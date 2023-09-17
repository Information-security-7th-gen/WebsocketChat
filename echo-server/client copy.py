import websocket, sys, threading

def on_message(client, message):
    file=open("other_message", "+w")
    print("Received:", message)
    print(message, file=file)
    file.close()

ws = websocket.WebSocketApp(f"ws://{sys.argv[1]}", on_message=on_message)
threading.Thread(target=ws.run_forever).start()

file=open("my_message", "+w")

while True:
    try:
        message = input("Enter a message: ")
        print(message, file=file)
    except (KeyboardInterrupt, EOFError):
        ws.close()
        file.close()
        break
    ws.send(message)
# wget http://192.168.1.30:8000/chat/client_log.py
# python3 client_log.py 192.168.0.16:8765