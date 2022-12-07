""" Types and Type Constructors """

class TypeVariable(object):

    NEXT_ID: int = 0

    def __init__(self) -> None:
        self.id = TypeVariable.NEXT_ID
        self.instance = None 
        self._name = None 

        TypeVariable.NEXT_ID += 1

    NEXT_VAR_NAME = 'a'

    @property 
    def name(self) -> str:
        if self.name is None:
            self._name = TypeVariable.NEXT_VAR_NAME
            TypeVariable.NEXT_VAR_NAME = chr(ord(TypeVariable.NEXT_VAR_NAME) + 1)

        return self._name

    def __str__(self) -> str:
        if self.instance is None:
            return self.name
        
        return str(self.instance)

    def __repr__(self) -> str:
        return f"TypeVariable(id = {self.id})"


class TypeOperator(object):
    def __init__(self, name, types) -> None:
        self.name = name
        self.types = types

    def __str__(self) -> str:
        num_types = len(self.types)

        match num_types:
            case 0:
                return self.name
            case 2:
                return f"({self.types[0]} {self.name} {self.types[1]}"
            case _:
                return f"({self.name} {' '.join(self.types)})"

class Function(TypeOperator):
    def __init__(self, from_type, to_type) -> None:
        super (Function, self).__init__('->', [from_type, to_type])

# Basic Types
Integer = TypeOperator('Int', [])
Boolean = TypeOperator('Bool', [])
