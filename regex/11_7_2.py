from re import findall, IGNORECASE

word = 'Familiarize'
row = 'stepik has such a good ui that it takes no time to familiarise its environment. To familiarize oneself with ui of stepik is easy'

pattern1 = fr'\W{word[0:-2]}[sz]e\W'

print(
    findall(pattern1, row, flags=IGNORECASE)
)