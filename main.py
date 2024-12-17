import webSocket

try:
    webSocket.run()
except KeyboardInterrupt:
    print("Terminated by user!")