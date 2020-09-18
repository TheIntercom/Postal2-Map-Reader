bitmask_dict = {0: 1 << 0,
                1: 1 << 1,
                2: 1 << 2,
                3: 1 << 3,
                4: 1 << 4,
                5: 1 << 5,
                6: 1 << 6,
                7: 1 << 7}
    
    ###################################

def bytes2hexlist(input_var):
	temp_list = list()

	for byte in input_var:
		temp_list.append("%0.2X" % byte)
        
	return temp_list