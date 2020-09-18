ENDIANORDER = 'little'

    ###################################
    
class GenericDataObject:
    def __init__(self, offset, name, data):
        self.offset = offset # int
        self.name = name # str
        self.data = data # byte/bytearray

    def to_int(self):
        return int.from_bytes(self.data, ENDIANORDER)

    def to_flag(self):
        return "0x{}".format(hex(int.from_bytes(self.data, ENDIANORDER))[2::].zfill(8))

    def size(self):
        return len(self.data)

    def __to_binary(self):
        output = list()
        temp_string = ''

        for byte in self.data:
            temp_string = format(byte, '#010b')
            output.append(temp_string)

        return output

    def __to_bytes(self):
        output = list()
        temp_string = ''

        for byte in self.data:
            temp_string = format(byte, '02X')
            output.append(temp_string)

        return output

    def print(self, data_key = ''):

        options = { '' : self.data,
                    'f': self.to_flag(),
                    'i': self.to_int(),
                    'bin': self.__to_binary(),
                    'bytes': self.__to_bytes(),
        }

        print("[{}] {}: {}".format(hex(self.offset), self.name, options[data_key]))