def min(args):
    min = args[0]
    for i in args:
        if i < min:
            min = i
    return min


def max(args):
    max = args[0]
    for i in args:
        if i > max:
            max = i
    return max


def len(args):
    len = 0
    for i in args:
        len += 1
    return len


def sum(args):
    sum = 0
    for i in args:
        sum += i
    return sum


def sorted(args):
    sort = []
    for i in args:
        sort.append(i)
    sort.sort()
    return sort


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
