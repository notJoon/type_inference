""" Exception classes for the application."""

class InferenceErr(Exception):
    """ raise error if inference fails """
    def __init__(self, msg: str) -> None:
        self.msg = msg

    @property
    def __str__(self) -> str:
        return str(self.msg)

class ParseError(Exception):
    """ raise error if environment is not fully applied """
    def __init__(self, msg: str) -> None:
        self.msg = msg 

    @property
    def __str__(self) -> str:
        return str(self.msg)