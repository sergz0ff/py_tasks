def parse_ranges(ranges):
    return (
        i 
        for elem in ranges.split(',')
        for i in range(int(elem.split('-')[0]), int(elem.split('-')[1]) + 1)
    )


print(*parse_ranges('1-2,4-4,8-10'))

print(*parse_ranges('1-10,2-10'))

print(*parse_ranges('7-32'))