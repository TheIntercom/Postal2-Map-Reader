from map_manager import MapManager
from table_manager import TableManager

	####################################

mm = MapManager()

for i in range(mm.length):
	f = mm.get_file_handle(i)

	tm = TableManager(f)
	embedded_object_list = tm.generate_embedded_object_list()

	f.close()

	print(f'Map: {mm.get_map_name(i)} -> Embedded Object 0')
	
	for k, v in vars(embedded_object_list[0]).items():
		print(f'{k}:	{v}')

	# print(f'{embedded_object_list.serial_data}')

	print('-' * 25)