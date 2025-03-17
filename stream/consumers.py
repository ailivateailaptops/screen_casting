import json
import base64
import numpy as np
import cv2
from channels.generic.websocket import AsyncWebsocketConsumer

active_streams = {}

class ScreenShareConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.client_ip = self.scope["client"][0]
        active_streams[self.client_ip] = self

        await self.accept()
        print(f"{self.client_ip} Connected and started sharing.")

        await self.send(text_data=json.dumps({
            "status": "connected",
            "message": "Screen sharing started."
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        if "image" in data:
            image_data = data["image"]

            try:
                img_bytes = base64.b64decode(image_data.split(',')[1])
                np_arr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                if frame is not None:
                    cv2.imshow(f"Screen from {self.client_ip}", frame)
                    cv2.waitKey(1)

            except Exception as e:
                print(f"Error decoding image: {e}")

    async def disconnect(self, close_code):
        print(f"{self.client_ip} Disconnected.")
        if self.client_ip in active_streams:
            del active_streams[self.client_ip]
        cv2.destroyAllWindows()
