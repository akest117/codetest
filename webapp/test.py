#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonProject1 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：shiqinqin
@Date    ：2024/6/5 11:03 
"""
import json
import threading

import websocket


def on_message(ws, message):
    print(f"Received: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    send_name(ws, "aaa")

def send_name(ws, name):
    ws.send(json.dumps({"username": name}))


def send_msg():
    for i in range(100):
        ws.send(f"test message {i}")
        time.sleep(3)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    threading.Thread(target=send_msg).start()
    ws.run_forever()
    pass