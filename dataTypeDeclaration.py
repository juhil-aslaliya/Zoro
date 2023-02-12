from dataclasses import dataclass
from fractions import Fraction
from typing import List



################################################################## DataTypes ##################################################################

@dataclass
class Frac:
    value: Fraction
    def __init__(self, *args) -> None:
        self.value = Fraction(*args)

@dataclass
class String:
    value: str
    def __init__(self, *args) -> None:
        self.value = str(*args)

@dataclass
class Float:
    value: float
    def __init__(self, *args) -> None:
        self.value = float(*args)

@dataclass
class Int:
    value: int
    def __init__(self, *args) -> None:
        self.value = int(*args)

@dataclass
class Bool:
    value: bool
    def __init__(self, *args) -> None:
        self.value = bool(*args)

################################################################## Operators ##################################################################

@dataclass
class Operator:
    op: str

@dataclass
class BinOp:
    operator: str
    left: 'AST'
    right: 'AST'

@dataclass
class MathOp:
    operator: str
    left: 'AST'
    right: 'AST'

@dataclass
class CndOp:
    operator: str
    left: 'AST'
    right: 'AST'

@dataclass
class UnOp:
    operator: str
    right: 'AST'

@dataclass
class BitOp:
    operator: str
    right: 'AST'
    left: 'AST'

@dataclass
class Assign:
    operator: str
    left: 'AST'
    right: 'AST'

############################################################# Identifier Classes #############################################################

@dataclass
class Variable:
    name: str

############################################################ Keywords Constructs #############################################################

@dataclass
class Sequence:
    seq: List['AST']

@dataclass
class Let:
    var: 'AST'
    e1: 'AST'
    e2: 'AST'

@dataclass
class If:
    con: List['AST']
    seq: List['AST']

########################################################### Identifier Constructs ############################################################

@dataclass
class Identifier:
    word: str

@dataclass
class Keyword:
    word: str






###############################################################################################################################################


AST = Int | Float | Bool | String | Frac    |    Operator | BinOp | MathOp | CndOp | UnOp | BitOp | Assign     |    Variable | Let | If | Sequence     

Token = Int | Float | Bool | String | Frac    |    Operator | BinOp | MathOp | CndOp | UnOp | BitOp | Assign     |     Let | If     

Value = Fraction | bool | int | float | str | None 


###############################################################################################################################################


keywords = "   if then elif else endif    let    Int Float String Bool Frac   ".split()

symbolic_operators = "  + - * / // % **    < <= => > == !=    >> <<    ~ & | ^     <- ->  ".split()

word_operators = " and or not xor xnor nand nor ".split()           # Logical Operators

whitespace = "\t \n".split() + [' ']


###############################################################################################################################################