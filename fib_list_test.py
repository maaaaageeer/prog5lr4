from fib_list import FibonacchiLst


def test_fibList1():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fb_list = FibonacchiLst(lst)

    res_lst = []
    for i in fb_list:
        res_lst.append(i)
    assert res_lst == [0, 1, 2, 3, 5, 8, 1], "Список [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]"

def test_fibList2():
    lst = [-1,-10, 77, 3419, 13, 1]
    fb_list = FibonacchiLst(lst)

    res_lst = []
    for i in fb_list:
        res_lst.append(i)
    assert res_lst == [13,1], "Список [-1,-10, 77, 3419, 13, 1]"


test_fibList1()
test_fibList2()