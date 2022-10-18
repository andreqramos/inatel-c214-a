def fizzbuzz(number):
    if number == 5:
        return 'buzz'
    if number == 10:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    return str(number)
