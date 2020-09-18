from os import listdir
	
	###################################

class MapManager:
	def __init__(self):
		super(MapManager, self).__init__()

		self.__map_prefix = '..\\Maps\\'

		self.map_list = listdir('..\\Maps')
		self.map_list = [f'{self.__map_prefix}{map}' for map in self.map_list]
		self.length = len(self.map_list)

	def get_file_handle(self, index):
		file_handle = open(self.map_list[index], 'rb')
		self.file_handle = file_handle
		return file_handle

	def close(self):
		self.file_handle.close()

	def get_map_name(self, index):
		return self.map_list[index][len(self.__map_prefix)::]

	###################################