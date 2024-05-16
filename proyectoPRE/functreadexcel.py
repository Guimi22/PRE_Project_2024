# v1.0 (12/05/2024): function to read .csv file.
# Notes on the v1.0 results: when reading a .csv file, each line is read column by column,
# returning values of each cell as strings separated with semicolon and ended in \n. Doctest not working.
#filename = 'Libro1.csv'
def functreadexcel(filename):
    '''
    >>> filename = 'Libro1.csv'
    >>> functreadexcel(filename)
    ['tu\n', 'holaaa\n', 'pe\n']

    '''

    with open(filename, mode = 'r') as f:
        lines_file = []
        for line in f:
            lines_file.append(line)
        print(lines_file)
    return lines_file

if __name__ == "functreadexcel":
    import doctest
    print(doctest.testmod())