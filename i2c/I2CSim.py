from .I2CBase import I2CBase

class I2CSim(I2CBase):
    def __init__(self, defaultAddress: int = None, defaultBusSpeed: int = 100000) -> None:
        super().__init__(defaultAddress)

    def scan(self):
        print('Scanning addresses. Found 0x04, 0x25')
        print('-------------------')
    
    def checkAddress(self, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Device at {addr:02X} found')
        print('-------------------')
    
    def write(self, data: list, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Writing {len(data)} {"bytes" if len(data) != 1 else "byte"} from buffer {data}; addr={addr:02X}')
        print('-------------------')
    
    def read(self, numBytes: int, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Reading {numBytes} {"bytes" if numBytes != 1 else "byte"} from addr={addr:02X}')
        print('-------------------')
    
    def writeThenRead(self, data: list, numBytes: int, address: int = None):
        print('Writing then reading:')
        self.write(data, address)
        self.read(numBytes, address)
        