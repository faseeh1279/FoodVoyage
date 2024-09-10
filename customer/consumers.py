from channels.consumer import SyncConsumer, StopConsumer
from asgiref.sync import async_to_sync
import json

class MySynConsumer(SyncConsumer): 
    def websocket_connect(self, event): 
        async_to_sync(self.channel_layer.group_add)(
            "order_placed", 
            self.channel_name 
        )
        self.send({
            "type":"websocket.accept", 
        })
        print("Connected...", event) 
    
    def websocket_receive(self, event):
        jsonData = json.loads(event["text"]) 
        username = jsonData.get("username")
        message = jsonData.get("message")
        time_stamp = jsonData.get("time_stamp")
        print("Client", event["text"])
        async_to_sync(self.channel_layer.group_send)(
            "order_placed",
            {
            "type":"place.order", 
            "username":username, 
            "message":message, 
            "time_stamp":time_stamp
            }
        )
        
    def place_order(self, event): 
        response_data = {
            "username":event["username"],
            "message":event["message"],
            "time_stamp":event["time_stamp"]
        }
        self.send({
            "type":"websocket.send", 
            "text":json.dumps(response_data) 
        })

    def websocket_disconnect(self, event): 
        print("Disconnected...", event) 
        async_to_sync(self.channel_layer.group_discard)(
            "order_placed", 
            self.channel_name 
        )
        raise StopConsumer() 