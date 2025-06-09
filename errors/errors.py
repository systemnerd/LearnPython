class RunTimeErrorCodeWithName(TypeError):
    """
        Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code
    

print("""
    Hello world? 
    how are you?
""")

raise RunTimeErrorCodeWithName("An error happened.", 500)