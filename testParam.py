def tupleParem(*t):
    print(t, type(t))


def dictParam(**d):
    print(d, type(d))


def accept1(*s):
    print(sum(s))
    print(sum(list1))


def accept2(**s):
    print(s)
    print(list2)

def mean(one,*other):
    '''
    把某函数接收到的除了第一个参数之外的所有参数输出
    '''
    print(other)

tupleParem((1, 2, 3))
dictParam(a=1, b=2)
list1 = (0, 1, 2, 3, 7.5)
list2 = {'a': 0, 'b': 1, 'c': 2}
accept1(*list1)
accept2(**list2)
mean('milk','oranage','branana')
