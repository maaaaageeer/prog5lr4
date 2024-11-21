import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res



def my_genn():
    """Сопрограмма"""
    while True:
        number_of_fib_elem = yield
        l = []
        # Реакция на недопустимые параметры
        continueCount = True
        if number_of_fib_elem == None or not isinstance(number_of_fib_elem,int) or number_of_fib_elem <= 0:
            continueCount = False
        # создание элементов ряда Фибоначчи
        counter = 0 #счетчик количества генераций ряда
        g = fib_elem_gen() #Перезапуск генератора
        while continueCount:
            el = next(g)
            counter+=1
            if counter > number_of_fib_elem:
                break
            l.append(el)
        yield l

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner

