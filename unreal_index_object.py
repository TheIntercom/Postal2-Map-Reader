from generic_data_object import GenericDataObject, ENDIANORDER

    ###################################

bitmask_dict = {0: 1 << 0,
                1: 1 << 1,
                2: 1 << 2,
                3: 1 << 3,
                4: 1 << 4,
                5: 1 << 5,
                6: 1 << 6,
                7: 1 << 7}
    
    ###################################

class UnrealIndexObject:
    def __init__(self, file_handle, offset):
        self.offset = offset

        file_handle.seek(self.offset)

        self.index_length = self.__get_index_length(file_handle, self.offset)
        self.raw_data = file_handle.read(self.index_length)
        self.index_value = self.__get_index_value()

    def __get_index_value(self):
        check_signed_byte = True

        signed = False
        temp_list = list()

        for byte in self.raw_data:
            padded_byte = bin(byte)[2::].zfill(8)

            if (check_signed_byte):
                check_signed_byte = False
                signed = (int(padded_byte, 2) & bitmask_dict[7])
                temp_list.append(padded_byte[2::])
            else:
                temp_list.append(padded_byte[1::])

        # if ENDIANORDER is 'little':
        temp_list.reverse()

        output = str().join(temp_list)

        if signed:
            output = f'-{output}'

        return int(output, 2)

    def __get_index_length(self, file_handle, index = -1):      
        if index < 0:
            index = file_handle.tell()

        file_handle.seek(index)

        temp_bytes = file_handle.read(5)

        check_first_byte = True

        length = 0

        for byte in temp_bytes:
            length += 1

            if check_first_byte:
                check_first_byte = False
                bitmask = bitmask_dict[6]
            else:
                bitmask = bitmask_dict[7]

            if not (byte & bitmask):
                break

        file_handle.seek(index)

        return length

    ###################################

class DWORDIndexObject:
    def __init__(self, file_handle, offset):
        super(DWORDIndexObject, self).__init__()

        __file_handle = file_handle
        self.offset = offset
        
        __file_handle.seek(self.offset)

        self.raw_data = __file_handle.read(4)

        self.dword_value = self.__get_dword()

    def __get_dword(self):
        # this bit stolen from: https://stackoverflow.com/a/9147327
        package_value = GenericDataObject(offset = -1, name = '', data = self.raw_data).to_int()

        if (package_value & (1 << (32 - 1))) != 0:
            package_value = package_value - (1 << 32)

        return package_value