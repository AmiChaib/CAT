class NoCategorySelectedException(Exception):
    """Exception raised for when no category is selected.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="You must select a category to analyse the text for."):
        self.message = message
        super().__init__(self.message)