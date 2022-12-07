""" class definition for AST nodes
which make up the little language for which types will be inferred.
"""

class Lambda(object):
    def __init__(self, var, body) -> None:
        self.var = var 
        self.body = body 

    def __str__(self) -> str:
        return f"(fn {self.var} -> {self.body})"

class Identifier(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

class Apply(object):
    """ Function Application """
    def __init__(self, func, arg) -> None:
        self.func = func 
        self.arg = arg 

    def __str__(self) -> str:
        return f"({self.func} {self.arg})"

class Let(object):
    def __init__(self, var, expr, body) -> None:
        self.var = var 
        self.expr = expr 
        self.body = body 

    def __str__(self) -> str:
        return f"(let {self.var} = {self.expr} in {self.body})"

class Letrec(object):
    def __init__(self, var, expr, body) -> None:
        self.var = var
        self.expr = expr
        self.body = body 

    def __str__(self) -> str:
        return f"(letrec {self.var} = {self.expr} in {self.body})"