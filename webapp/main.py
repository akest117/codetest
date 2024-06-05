#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test
@File    ：main.py
@IDE     ：PyCharm
@Author  ：shiqinqin
@Date    ：2024/6/4 13:33
"""
import json

from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect


class ConnectionManager:
    def __init__(self):
        self.active_connections: set = set()
        self.user_dict: dict = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    async def get_username(self, websocket: WebSocket):
        # 接收用户名
        username_data = await websocket.receive_text()
        username = json.loads(username_data).get("username")
        if username is None or username in self.user_dict:
            print("1003")
            await websocket.close(code=1003)  # 不合法或重复的用户名，关闭连接
            return False
        self.user_dict[username] = websocket

        return username

    def disconnect(self, websocket: WebSocket, username: str):
        self.active_connections.discard(websocket)
        del self.user_dict[username]  # 删除用户名

    async def broadcast(self, websocket: WebSocket, message: str):
        for conn in self.active_connections:
            if conn is not websocket:  # 不发送给自己
                await conn.send_text(message)


manager = ConnectionManager()

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    username = await manager.get_username(websocket)
    if username is False:
        return
    try:
        async for message in websocket.iter_text():
            broadcast_message = f"{username}: {message}"
            await manager.broadcast(websocket, broadcast_message)
    except WebSocketDisconnect:
        print("error close")
    finally:
        manager.disconnect(websocket, username)


if __name__ == "__main__":
    print("start")
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
