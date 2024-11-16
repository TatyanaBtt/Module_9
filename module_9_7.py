def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        prime = True
        for j in range(2, result):
            if result % j == 0:
                prime = False
            break
        if prime:
            print('Простое')
            return result
        else:
            print('Составное')
            return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    rez = a + b + c
    return rez


result = sum_three(11, 12, 5)
print(result)
