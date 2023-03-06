a : int = 5
b : str = 'строка'
c : list = [1, 2]

def indent(s: str, width: int) -> str:
    return "" * (max(0, width - len(s))) + s

print(indent('123', 123))


def line(s: str = "") -> int:
    return len(s)
print(line('boo'))

def arg(x: list, y: list) -> int:
    return max(len(x), len(y))
print(arg([1,2], [1, 2, 3, 4]))