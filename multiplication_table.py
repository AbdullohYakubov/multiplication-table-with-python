for i in range(1, 11):
    # top row 
    if i == 1:
        print('*', end = '\t')
        for j in range(1, 11):
            print(j, end = '\t')
    # first column 
    print('\n', i, sep = '', end = '\t')
    # multiplication results
    for j in range(1, 11):
        print(i*j, end = '\t')