def is_prime(number):
    # counter = 0
    # for i in range(1, number + 1):
    #     if number % i == 0:
    #         counter += 1
    # if counter == 2:
    #     return True
    # else:
    #     return False
    # nums = (True for i in range(1, number + 1) if number % i == 0)
    # if len(list(nums)) == 2:
    #     return True
    # else:
    #     return False
    print([number % i for i in range(2, number)])
    print(all([number % i for i in range(2, number)]))

print(is_prime(2))