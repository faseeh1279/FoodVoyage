from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer): 
    def websocket_connect(self, event): 
        print("Connected",event)

    def websocket_receive(self,event): 
        print("Message Received from Customer:",event)

    def websocket_disconnect(self,event): 
        print("Disconnected",event)