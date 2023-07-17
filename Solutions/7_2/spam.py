from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass
