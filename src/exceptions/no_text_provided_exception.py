class NoTextProvidedException(Exception):
    """Exception raised for when no input text is given.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="You must give a text to analyse."):
        self.message = message
        super().__init__(self.message)