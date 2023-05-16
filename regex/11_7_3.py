from re import findall, IGNORECASE

# def abbreviate(phrase):
#     return findall(r"")
res = findall(r"\b(\w)[a-z]*([A-Z])?\w*\b", 'javaScript object notation')
print(
    ''.join((a + b).upper() for a,b in res)
)