#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    # n = n - 2
    # a = 1
    # b = 1
    # while n > 0:
    #     temp = a
    #     a = b
    #     b = temp + b
    #     n = n - 1
    # return b
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current





print fibonacci(60)
#>>> 14930352
