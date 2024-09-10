from channels.consumer import SyncConsumer, StopConsumer
from asgiref.sync import async_to_sync
import json

class MySyncConsumer(SyncConsumer): 
    def websocket_connect(self, event): 
        print("Connected", event)
        async_to_sync(self.channel_layer.group_add)(
            "placing_order", 
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        jsonData = json.loads(event['text'])
        print("Received JSON:", jsonData)  # Debugging line
        username = jsonData.get("username")
        message = jsonData.get("message")
        time_stamp = jsonData.get("time_stamp")
        async_to_sync(self.channel_layer.group_send)(
            "placing_order",
            {
                "type": "placing.order",
                "username": username, 
                "message": message, 
                "time_stamp": time_stamp
            }
        )

    def placing_order(self, event):
        response_data = {
            "username": event["username"],
            "message": event["message"],
            "time_stamp": event["time_stamp"]
        }
        self.send({
            'type': 'websocket.send',
            'text': json.dumps(response_data)
        })

    def websocket_disconnect(self, event):
        print("Disconnected", event)
        async_to_sync(self.channel_layer.group_discard)(
            "placing_order",
            self.channel_name
        )
        raise StopConsumer()
