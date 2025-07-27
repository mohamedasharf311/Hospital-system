import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

clients = set()

async def notify_clients(message):
    if clients:
        await asyncio.wait([client.send(message) for client in clients])

async def handler(websocket, path):
    logging.info(f"New connection from {websocket.remote_address}")
    clients.add(websocket)
    try:
        async for message in websocket:
            logging.info(f"Received message: {message}")
            await notify_clients(message)
    finally:
        clients.remove(websocket)
        logging.info(f"Connection closed from {websocket.remote_address}")

async def start_server():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        logging.info("WebSocket server started on port 8765")
        await asyncio.Future()  # Run forever

