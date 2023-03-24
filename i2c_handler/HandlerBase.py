from i2c.I2CBase import I2CBase

class HandlerBase(object):
    def __init__(self, action: dict, mandatoryKeys: list[str], i2c: I2CBase, defaultDelay: int = 0) -> None:
        self.mandatoryKeys = mandatoryKeys
        self.checkKeys()
        self.action = action
        self.name = action['action']
        self.addr = int(action['address'], base=16) if 'address' in action \
            else None
        self.i2c = i2c
        self.delay = defaultDelay
        if 'delay' in action:
            self.delay = action['delay']

    def handle(self):
        raise NotImplementedError
    
    def checkKeys(self, action: dict):
        for key in self.mandatoryKeys:
            if key not in action:
                raise KeyError
            
    def printLogMessage(self):
        if 'log_message' in self.action:
            print(f'[{self.name}] {self.action["log_message"]}')