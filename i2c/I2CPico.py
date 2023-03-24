from .I2CBase import I2CBase
import board
import busio

class I2CPico(I2CBase):
    def __init__(self, defaultAddress: int = None, defaultBusSpeed: int = 100000) -> None:
        super().__init__(defaultAddress)
        self.i2c = busio.I2C(board.SCL0, board.SDA0, defaultBusSpeed)
        while not self.i2c.try_lock():
            pass

    def scan(self):
        print('Starting scan')
        print("I2C addresses found:", [hex(device_address) for device_address in self.i2c.scan()])
    
    def checkAddress(self, address: int = None):
        addr = address if address is not None else self.defaultAddress
        self.i2c.writeto(addr, b'')
        print(f'Checked existence of device at {hex(addr)}')
    
    def write(self, data: list, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Writing {len(data)} {"bytes" if len(data) != 1 else "byte"} from buffer {data}; addr={hex(addr)}')
        self.i2c.writeto(addr, bytes(data))
    
    def read(self, numBytes: int, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Reading {numBytes} {"bytes" if numBytes != 1 else "byte"} from addr={hex(addr)}')
        buffer = bytearray(numBytes)
        self.i2c.readfrom_into(addr, buffer)
        print(f'Read bytes={buffer}')
    
    def writeThenRead(self, data: list, numBytes: int, address: int = None):
        addr = address if address is not None else self.defaultAddress
        print(f'Writing {data} then reading from addr={hex(addr)}')
        buffer = bytearray(numBytes)
        self.i2c.writeto_then_readfrom(addr, bytes(data), buffer)
        print(f'Read bytes={buffer}')