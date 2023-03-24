from .HandlerBase import HandlerBase
from i2c.I2CBase import I2CBase
import time

class HandleScan(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action'], i2c, defaultDelay)
    
    def handle(self):
        self.printLogMessage()
        self.i2c.scan()
        time.sleep(self.delay)
        
class HandleCheck(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action'], i2c, defaultDelay)
    
    def handle(self):
        self.printLogMessage()
        self.i2c.checkAddress(self.addr)
        time.sleep(self.delay)
        
class HandleWrite(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action', 'data'], i2c, defaultDelay)
    
    def handle(self):
        self.printLogMessage()
        self.i2c.write(self.action['data'], self.addr)
        time.sleep(self.delay)
        
class HandleRead(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action', 'bytes_to_read'], i2c, defaultDelay)
    
    def handle(self):
        self.printLogMessage()
        self.i2c.read(self.action['bytes_to_read'], self.addr)
        time.sleep(self.delay)
        
class HandleWriteThenRead(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action', 'data', 'bytes_to_read'], i2c, defaultDelay)
    
    def handle(self):
        self.printLogMessage()
        self.i2c.writeThenRead(self.action['data'], self.action['bytes_to_read'], self.addr)
        time.sleep(self.delay)
        
class HandleRepeat(HandlerBase):
    def __init__(self, action: dict, i2c: I2CBase, defaultDelay: float = 0) -> None:
        super().__init__(action, ['action', 'steps', 'times'], i2c, defaultDelay)
    
    def handle(self, factoryFunc):
        self.printLogMessage()
        
        for i in range(self.action['times']):
            for step in self.action['steps']:
                factoryFunc(step, self.i2c, self.delay)
        
def HandlerFactory(action: dict, i2c: I2CBase, defaultDelay: float = 0):
    actionType = action['action']
    
    if actionType == 'SCAN':
        HandleScan(action, i2c, defaultDelay).handle()
    elif actionType == 'CHECK_ADDR':
        HandleCheck(action, i2c, defaultDelay).handle()
    elif actionType == 'WRITE':
        HandleWrite(action, i2c, defaultDelay).handle()
    elif actionType == 'READ':
        HandleRead(action, i2c, defaultDelay).handle()
    elif actionType == 'WRITE_THEN_READ':
        HandleWriteThenRead(action, i2c, defaultDelay).handle()
    elif actionType == 'REPEAT':
        HandleRepeat(action, i2c, defaultDelay).handle(HandlerFactory)