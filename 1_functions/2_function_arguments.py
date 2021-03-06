# Позиционные, обязательные
def example_pos(a, b):
    print("a:", a, "b:", b)


# Именованные (имеющие значения по умолчанию)
def example_name(a=1, b=1):
    pass


# Комбинированная сигнатура
def foo(a, b=1):
    return a + b


# Передача по имени
example_pos(b=10, a=12)

"""
!Позиционные, могут идти ТОЛЬКО ПЕРЕД именованными,
как в сигнатуре так и при вызове функции
"""

# Функция принимающая любое количество неименованных аргументов
print("=== Любое количество позиционных аргументов ===")


def any_pos_args(*args):
    print(args)


any_pos_args(1, 2, 3, 4)

# Функция принимающая любое количество именованных аргументов
print("=== Любое количество именованных аргументов ===")


def any_kwargs(**kwargs):
    print(kwargs)


any_kwargs(test=1, money=2, something=10)

# Функция принимающая любое количество любых аргументов
# Первыми нужно передавать позиционные, потом именованные
print("=== Любое количество любых аргументов, c учетом правил ===")


def any_of_any(*args, **kwargs):
    print(args)
    print(kwargs)


any_of_any(1, 2, 3, 4, test=1, money=2)

# Распаковка значений при передаче в функцию
print("=== Распаковка значений из списков ===")


def foo_position(*args):
    print(args)


def foo_named(k1, k2):
    print(k1, k2)


l = [1, 2, 3]
d = {"k1": "v1", "k2": "v2"}

foo_position(*l)
foo_named(**d)
