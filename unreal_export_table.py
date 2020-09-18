from generic_data_object import GenericDataObject
from unreal_index_object import UnrealIndexObject, DWORDIndexObject

'''
INDEX // Class // Class of the Object. See “object references”. 
INDEX // Super // Parent of the Object (from which it inherits). See “object references”. 
DWORD // Package // Package this Object resides in. Could be an internal package (a group). See “object references”. 
INDEX // Object Name // The Object name. It’s an index into the Name Table. 
DWORD // Object Flags // See “Object Flags” 
INDEX // Serial Size // Size of the object inside the file. 
INDEX // Serial Offset // Offset of the object inside the file. This field only exists if SerialSize>0 
'''

class UnrealExportTable:
	def __init__(self, file_handle, export_count, export_table_offset):
		super(UnrealExportTable, self).__init__()

		self.count = export_count # int
		self.table_offset = export_table_offset # int

		file_handle.seek(self.table_offset)

		self.table = list()

		for i in range(0, self.count):
			output = self.ExportTableItem(file_handle, file_handle.tell())
			self.table.append(output)

	def get_table_item(self, index):
		return self.table[index]

	###################################

	class ExportTableItem:
		def __init__(self, file_handle, offset):
			# super(self.ExportTableItem, self).__init__() # it uses the wrong self so it freaks out, not to sure if i even really need this
			self.object_class	= UnrealIndexObject(file_handle, offset) # object reference
			self.object_parent	= UnrealIndexObject(file_handle, file_handle.tell()) # object reference
			self.package		= DWORDIndexObject(file_handle, file_handle.tell()) # object reference
			self.object_name	= UnrealIndexObject(file_handle, file_handle.tell()) # name table
			self.object_flag	= GenericDataObject(offset = -1, name = '', data = file_handle.read(4)) # to_flag
			self.serial_size	= UnrealIndexObject(file_handle, file_handle.tell()) # size in bytes(?) of data
			self.serial_offset	= None # offset of data

			if (self.serial_size.index_value > 0):
				self.serial_offset	= UnrealIndexObject(file_handle, file_handle.tell())

		def __iter__(self):
			return (t for t in self.properties)

		def get_object_name_value(self):
			return self.object_name.index_value

	###################################