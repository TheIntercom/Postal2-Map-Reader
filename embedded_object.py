class EmbeddedObject:
    def __init__(self):
        super(EmbeddedObject, self).__init__()
        
        self.object_class   = '' # str
        self.object_parent  = '' # str
        self.package        = '' # str
        self.object_name    = '' # str
        self.object_flag    = '' # str (hex)
        self.serial_size    = 0 # int (number of bytes)
        self.serial_offset  = 0 # int (dec)
        self.serial_data    = bytes()

    ###################################