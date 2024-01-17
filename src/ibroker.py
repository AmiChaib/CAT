from abc import ABC, abstractmethod # abstract base class

class IBroker(ABC):
    @abstractmethod
    def set_client(self, client):
        pass
    