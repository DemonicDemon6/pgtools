from typing import Any

class ErrorMessage:
    RED = "\033[91m"
    RESET = "\033[0m"

    def __call__(cls, *args, **kwargs):
        cls.InitiateError(cls.__name__)

    @classmethod 
    def TypeError(cls, var:str, expected:type, data:type):
        raise TypeError(f"{cls.RED}Expected {var} as {expected}. Got {data}{cls.RESET}")

    @classmethod 
    def LengthError(cls, var:str, expected:int, data:int):
        raise ValueError(f"{cls.RED}Expected {var} to have {expected} arguments. Got {data}{cls.RESET}")

    @classmethod 
    def RangeError(cls, var:str, min:int, max:int, data:any):
        raise ValueError(f"{cls.RED}Expected {var} to be in range {min}-{max}. Got {data}{cls.RESET}")
    
    @classmethod
    def FormatError(cls, var:str, form:str, data:any):
        raise ValueError(f"{cls.RED}Expected {var} to be in form {form}. Got {data}")
    
    @classmethod
    def InitiateError(cls, name:str):
        raise TypeError(f"{cls.RED}{name} class cannot be instantiated{cls.RESET}")