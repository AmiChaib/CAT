from abc import ABC # abstract base class

class Iresponse_processor(ABC):
    @abstractmethod
    def __init__(self):
        