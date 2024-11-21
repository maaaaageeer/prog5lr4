from fib import my_genn as mng ,fib_coroutine



def test_fib_1():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

    
def test_fib_2():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_3():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь первых членов ряда"


def test_fib_4():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send(0) == [], "Ноль первых членов ряда Фибоначчи"

def test_fib_5():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send('Пять') == [], "Недопустимый тип количества членов ряда Фибоначчи"

def test_fib_6():
    my_gen = fib_coroutine(mng)
    gen = my_gen()
    assert gen.send(-113) == [], "Отрицательное количество первых членов ряда Фибоначчи"

test_fib_1()
test_fib_2()
test_fib_3()
test_fib_4()
test_fib_5()
test_fib_6()
# здесь необходимо дополнительно написать несколько тестов для крайних случаев, которые могут возникнуть