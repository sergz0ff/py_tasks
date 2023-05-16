from itertools import product
from string import ascii_uppercase as letters

n = int(input())
m = int(input())
system = [i for i in range(10)] + [s for s in letters[:6]]
res = (''.join(map(str, nums)) for nums in product(system[:n], repeat=m))
print(*res)