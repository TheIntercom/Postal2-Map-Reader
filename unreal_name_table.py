from generic_data_object import GenericDataObject, ENDIANORDER

class UnrealNameTable:
    def __init__(self, file_handle, name_count, name_table_offset):
        self.count = name_count # int
        self.table_offset = name_table_offset # int

        file_handle.seek(self.table_offset)

        self.table = list()

        for i in range(0, self.count):
            self.temp_offset = file_handle.tell()
            self.temp_length = int.from_bytes(file_handle.read(1), ENDIANORDER)
            self.temp_name = file_handle.read(self.temp_length)
            self.temp_flags = file_handle.read(4)

            encoding = 'utf-8'
            output = GenericDataObject(offset = self.temp_offset, name = self.temp_name.decode(encoding)[0:(self.temp_length - 1)], data = self.temp_flags)

            self.table.append(output)

    def get_object_offset(self, index):
        return self.table[index].offset

    def get_object_name(self, index):
        return self.table[index].name

    def get_object_flags(self, index):
        return self.table[index].to_flag()

    def get_table_item(self, index):
        return self.table[index]
