import asyncio
import websockets
import struct

import functionProvider as fp

async def handler(websocket):
    print("Client connected")
    try:
        while True:
            # Receive binary data (2 bytes)
            message = await websocket.recv()

            # Unpack the two bytes
            received_bytes = struct.unpack("BB", message)  # Unpack two unsigned bytes
            function_call = received_bytes[0]  # First byte for function calls
            additional_info = received_bytes[1] & 0b11111  # Extract last 5 bits of second byte

            print(f"Received: Function Call={function_call}, Additional Info={additional_info}")

            # Example: Handle the function call
            if function_call >= 0:
                print(f"Executing function for call ID {function_call}...")
                
                fp.callFunc(function_call, additional_info)
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Keeps the server running indefinitely

asyncio.run(main())