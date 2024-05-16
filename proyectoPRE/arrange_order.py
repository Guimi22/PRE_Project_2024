#v1.0: method of the class item to rearenge the order so the robot runs shortest route

def arange_order(order):
	order_new = []
	for item in order:
		pos_aux = item[0].pos
		long = len(order_new)
		if pos_aux[0] < order_new[long]:
			order_new[long+1] = order_new[long]
			order_new[long] = item
		else:
			if pos_aux[1] < order_new[long]:
				order_new[long+1] = order_new[long]
				order_new[long] = item
			else:
				order_new.append(item)
	return order_new