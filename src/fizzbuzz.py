def fizzbuzz(number):
    try:
        number = int(number)
    except BaseException:
        raise  Exception("A entrada precisa ser um número")

    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'

    return str(number)
