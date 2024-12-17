import asyncio
import websockets
import struct
import functionProvider as fp

active_sockets = {}  # Dictionary to track active sockets

async def send_distance(websocket, distance):
    try:
        await websocket.send(f"Distance: {distance:.2f} cm")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed while sending data.")

async def handler(websocket):
    print("Client connected")
    client_id = id(websocket)  # Use websocket's unique ID as the key
    active_sockets[client_id] = websocket

    try:
        while True:
            # Receive binary data (2 bytes)
            message = await websocket.recv()
            readMessage(message, websocket)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        del active_sockets[client_id]  # Remove the client on disconnect

def readMessage(message, websocket):
    """
    Unpack and process the received message.

    Parameters:
        message (bytes): The raw message data in bytes format.
        websocket: The client socket to send data to.
    """
    funcCall, objID, pin0, pin1 = struct.unpack("BBBB", message)
    print(f"Received: Function Call={funcCall}, ObjID={objID}, Pin0={pin0}, Pin1={pin1}")

    if funcCall == 3:
        # Pass a callback function to send data
        fp.callFunc(funcCall, objID, pin0, lambda distance: asyncio.create_task(send_distance(websocket, distance)))
    else:
        fp.callFunc(funcCall, objID, pin0, pin1)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # Keeps the server running indefinitely

def run():
    asyncio.run(main())
