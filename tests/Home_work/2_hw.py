def task_1() -> any:
    q: int = 7
    p: float = 3.6
    r: str = 'boo'
    t: list = [6, 7]
    w: bool = True
    print(type(q), type(p), type(r), type(t), type(w))
task_1()


def task_2() -> list:
    a=[1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(task_2()) # В списке натуральный ряд чисел.


def task_3(h) -> int:
    return h ** 2
print(task_3(4))
