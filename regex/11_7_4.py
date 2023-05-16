from re import findall

pattern1 = r"<a href=\"(.+)\">(.+)</a>"
for line in open(0):
    for i in findall(pattern1, line):
        print(i[0], i[1])
