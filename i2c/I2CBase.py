class I2CBase(object):
    def __init__(self, defaultAddress: int = None) -> None:
        self.defaultAddress = defaultAddress

    def scan(self):
        raise NotImplementedError
    
    def checkAddress(self, address: int = None):
        raise NotImplementedError
    
    def write(self, data: list, address: int = None):
        raise NotImplementedError
    
    def read(self, numBytes: int, address: int = None):
        raise NotImplementedError
    
    def writeThenRead(self, data: list, numBytes: int, address: int = None):
        raise NotImplementedError