from re import findall

# row = input()
row = 'existing pessimist optimist this is'
# word = input()
word = 'is'
pattern1 = fr'\w+{word}\w+'

print(
    len(findall(pattern1, row))
)