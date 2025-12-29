class InvalidArgumentError(Exception):

    def __init__(self, message="Invalid argument provided.", params=None):
        self.message = message
        self.params = params or {}
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} {self.params}"

    def __repr__(self):
        return f"InvalidArgumentError(message='{self.message}', params={self.params})"
