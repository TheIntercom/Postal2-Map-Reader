from unreal_package_header import UnrealPackageHeader
from unreal_name_table import UnrealNameTable
from unreal_export_table import UnrealExportTable
from unreal_import_table import UnrealImportTable

from embedded_object import EmbeddedObject

from util import bytes2list

    ###################################

class TableManager:
    def __init__(self, file_handle):
        self.__file_handle = file_handle # just so i can be lazy with generating the embedded object list

        self.unreal_header = UnrealPackageHeader(file_handle)

        self.name_count = self.unreal_header.get_name_count()
        self.export_count = self.unreal_header.get_export_count()
        self.import_count = self.unreal_header.get_import_count()

        self.name_table_offset = self.unreal_header.get_name_table_offset()
        self.export_table_offset = self.unreal_header.get_export_table_offset()
        self.import_table_offset = self.unreal_header.get_import_table_offset()

        self.name_table = UnrealNameTable(file_handle, self.name_count, self.name_table_offset)
        self.export_table = UnrealExportTable(file_handle, self.export_count, self.export_table_offset)
        self.import_table = UnrealImportTable(file_handle, self.import_count, self.import_table_offset)

    def generate_embedded_object_list(self):
        output = list()

        for table_item in self.export_table.table:
            temp_object = EmbeddedObject()

            temp_object.object_class    = self.__follow_object_reference(table_item.object_class.index_value) # object reference
            temp_object.object_parent   = self.__follow_object_reference(table_item.object_parent.index_value) # object reference
            temp_object.package         = self.__follow_object_reference(table_item.package.dword_value) # object reference
            temp_object.object_name     = self.__get_name_from_table(table_item.object_name.index_value) # name table
            temp_object.object_flag     = table_item.object_flag.to_flag() # str -> 0x01234567
            temp_object.serial_size     = table_item.serial_size.index_value # int
            temp_object.serial_offset   = table_item.serial_offset.index_value # int

            self.__file_handle.seek(temp_object.serial_offset)

            temp_object.serial_data     = bytes2list(self.__file_handle.read(temp_object.serial_size))

            # if ENDIANORDER is 'little':
            temp_object.serial_data.reverse()

            output.append(temp_object)

        return output

    def __follow_object_reference(self, index):
        '''
        If the index is zero the object referenced is null. 
        If the index<0 the object is in the Import table in the position (–index-1). 
        If the index>0 the object is in the Export table in the position (index-1). 
        '''
        if (index < 0):
            index *= -1
            return self.__get_name_from_table(self.import_table.get_table_item(index - 1).get_object_name_value())
        elif (index > 0):
            return self.__get_name_from_table(self.export_table.get_table_item(index - 1).get_object_name_value())
        else:
            return 'Null' # i don't know what this really means for the object but we'll track it nonetheless

    def __get_name_from_table(self, index):
        return self.name_table.get_object_name(index)