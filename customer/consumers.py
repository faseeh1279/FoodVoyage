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
        customer_name = jsonData.get("customer_name")
        message = jsonData.get("message")
        time_stamp = jsonData.get("time_stamp")
        customer_id = jsonData.get("customer_id")
        customer_location = jsonData.get("customer_location")
        rider = jsonData.get("rider") 
        async_to_sync(self.channel_layer.group_send)(
            "order_placed",
            {
                "type": "place.order",
                "customer_name": customer_name,
                "message": message,
                "time_stamp": time_stamp,
                "customer_id": customer_id, 
                "customer_location":customer_location, 
                "rider":rider
            }
        )
        
    def place_order(self, event): 
        response_data = {
            "customer_name":event["customer_name"], 
            "message":event["message"], 
            "time_stamp":event["time_stamp"],
            "customer_id":event["customer_id"], 
            "customer_location":event["customer_location"],
            "rider":event["rider"]
        }
        self.send({
            "type":"websocket.send",
            "text": json.dumps(response_data)
            })
        

    def websocket_disconnect(self, event): 
        print("Disconnected...", event) 
        async_to_sync(self.channel_layer.group_discard)(
            "order_placed", 
            self.channel_name 
        )
        raise StopConsumer() 