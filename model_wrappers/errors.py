class FieldDoesNotExist(Exception):
    def __init__(self, **kwargs):
        super().__init__(f"{self.__class__.__name__}: {kwargs}")
