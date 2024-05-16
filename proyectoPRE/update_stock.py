

def update_stock(filename):
    with open(filename, mode = 'r') as f:
        lines_aux1 = []
        lines_aux2 = []
        list_stock = []
        for line in f:
            lines_aux1 = line.split(';')
            len_line = len(lines_aux1)
            lines_aux2 = lines_aux1[len_line-1].split('\n')
            lines_aux2.remove('')
            lines_aux1.remove(lines_aux1[len_line-1])
            lines_aux1.append(lines_aux2)
            list_stock.append(lines_aux1)
    return list_stock