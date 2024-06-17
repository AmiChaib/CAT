from client import Client

class Container():
    def __init__(self, client):
        self.client = client
        
client = Client()
container = Container(client)