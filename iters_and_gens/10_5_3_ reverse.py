# def reverse(sequence):
#     count = len(sequence)
#     for i in range(1, count + 1):
#         yield sequence[-i]

def reverse(sequence):
    count = len(sequence)
    for i in sequence[::-1]:
        yield i

print(*reverse([1, 2, 3, 4, 5]))