from generic_data_object import GenericDataObject

class UnrealPackageHeader:
    def __init__(self, file_handle):
        self.file_handle = file_handle

        ###############################################
        # general header information for unreal packages
        self.unreal_signature = GenericDataObject(offset = self.file_handle.tell(), name = "unreal_signature", data = self.file_handle.read(4)) # magic number, i suppose i should ensure we're checking an unreal package at some point

        self.version = GenericDataObject(offset = self.file_handle.tell(), name = "version", data = self.file_handle.read(2)) # shows what version of unreal the package is for
        self.licensee_mode = GenericDataObject(offset = self.file_handle.tell(), name = "licensee_mode", data = self.file_handle.read(2)) # seems unused

        self.package_flags = GenericDataObject(offset = self.file_handle.tell(), name = "package_flags", data = self.file_handle.read(4))

        self.name_count = GenericDataObject(offset = self.file_handle.tell(), name = "name_count", data = self.file_handle.read(4)) # (0, number - 1) inclusive for accurate total representation
        self.name_table_offset = GenericDataObject(offset = self.file_handle.tell(), name = "name_table_offset", data = self.file_handle.read(4)) # offset is from start of file

        self.export_count = GenericDataObject(offset = self.file_handle.tell(), name = "export_count", data = self.file_handle.read(4))
        self.export_table_offset = GenericDataObject(offset = self.file_handle.tell(), name = "export_table_offset", data = self.file_handle.read(4)) # offset is (apparently) absolute

        self.import_count = GenericDataObject(offset = self.file_handle.tell(), name = "import_count", data = self.file_handle.read(4))
        self.import_table_offset = GenericDataObject(offset = self.file_handle.tell(), name = "import_table_offset", data = self.file_handle.read(4)) # offset is (apparently) absolute

        self.guid = GenericDataObject(offset = self.file_handle.tell(), name = "guid", data = self.file_handle.read(16)) # idk what this is for

        ###############################################
        # generation information
        # for detecting general differences between versions of the same map for online play
        self.generation_count = GenericDataObject(offset = self.file_handle.tell(), name = "generation_count", data = self.file_handle.read(4)) # idk what this is
        self.generation_export_count = GenericDataObject(offset = self.file_handle.tell(), name = "generation_export_count", data = self.file_handle.read(4)) # seems to be a copy of 'export_count'
        self.generation_name_count = GenericDataObject(offset = self.file_handle.tell(), name = "generation_name_count", data = self.file_handle.read(4)) # seems to be a copy of 'name_count'


    def get_name_count(self):
        return self.name_count.to_int()
    def get_name_table_offset(self):
        return self.name_table_offset.to_int()

    def get_export_count(self):
        return self.export_count.to_int()
    def get_export_table_offset(self):
        return self.export_table_offset.to_int()

    def get_import_count(self):
        return self.import_count.to_int()
    def get_import_table_offset(self):
        return self.import_table_offset.to_int()

