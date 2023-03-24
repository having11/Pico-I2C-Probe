from I2CBase import I2CBase

class I2CSim(I2CBase):
    def __init__(self, defaultAddress: int = None) -> None:
        super(defaultAddress)

    def scan(self):
        print('Scanning addresses. Found 0x04, 0x25')
    
    def checkAddress(self, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Device at {addr:02X} found')
    
    def write(self, data: list, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Writing {len(data)} bytes from {data}; addr={addr:02X}')
    
    def read(self, numBytes: int, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Reading {numBytes} from addr={addr:02X}')
    
    def writeThenRead(self, data: list, numBytes: int, address: int = None):
        print('Writing then reading')
        self.write(data, address)
        self.read(numBytes, address)
        