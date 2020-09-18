from generic_data_object import GenericDataObject
from unreal_index_object import UnrealIndexObject, DWORDIndexObject

'''
INDEX // Class Package // Package of the Class. It’s an index into the Name Table. 
INDEX // Class Name // The Class of the Object. It’s an index into the Name Table. 
DWORD // Package // The Package this object resides in. See “object references”. 
INDEX // Object Name // The Object name. It’s an index into the Name Table. '''

class UnrealImportTable:
    def __init__(self, file_handle, import_count, import_table_offset):
        super(UnrealImportTable, self).__init__()

        __file_handle = file_handle
        self.count = import_count # int
        self.table_offset = import_table_offset # int

        __file_handle.seek(self.table_offset)

        self.table = list()

        for i in range(0, self.count):
            output = self.ImportTableItem(__file_handle, __file_handle.tell())
            self.table.append(output)

    def get_table_item(self, index):
        return self.table[index]

    ###################################
    
    class ImportTableItem:
        def __init__(self, file_handle, offset):
            # super(self.ImportTableItem, self).__init__() # it uses the wrong self so it freaks out, not to sure if i even really need this
            self.class_package      = UnrealIndexObject(file_handle, offset) # name table
            self.class_name         = UnrealIndexObject(file_handle, file_handle.tell()) # name table
            self.package            = DWORDIndexObject(file_handle, file_handle.tell()) # object reference
            self.object_name        = UnrealIndexObject(file_handle, file_handle.tell()) # name table

        def __iter__(self):
            return (t for t in self.properties)

        def get_object_name_value(self):
            return self.object_name.index_value

    ###################################