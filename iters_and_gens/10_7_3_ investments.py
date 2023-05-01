with open('iters_and_gens/data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)
    result = 0
    for a in line_dicts:
        if a['round'] == 'a':
            result += int(a['raisedAmt'])
    print(result)
    # result = (int(line['raisedAmt'])
    #           for line in line_dicts
    #           if line['round'] == 'a')
    # print(sum(result))