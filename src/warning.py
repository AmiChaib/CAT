class Warning():
    def __init__(self):
        self.is_warning = False
        self.content = None
        
    def set_warning(self, is_warning, warning_content):        
        self.is_warning = is_warning
        self.content = warning_content
        
warning = Warning()