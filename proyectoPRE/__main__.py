# v1.0: function to read orders and add them to the almacen

def funct_read_order(filename):
    '''
    >>> filename = 'Libro1.csv'
    >>> funct_read_order(filename)
    [['5433fg', '5'], ['55572f', '6'], ['37441d', '7']]
    '''
    with open(filename, mode = 'r') as f:
        lines_aux1 = []
        lines_aux2 = []
        lines_aux3 = []
        list_order = []
        for line in f:
            lines_aux1 = line.split(';')
            lines_aux2 = lines_aux1[1].split('\n')
            lines_aux2.remove('')
            lines_aux3 = [lines_aux1[0],lines_aux2[0]]
            list_order.append(lines_aux3)
    return list_order

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())