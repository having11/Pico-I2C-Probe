import json
from i2c.I2CPico import I2CPico
from i2c_handler.Handlers import HandlerFactory

actionsPath = './actions.json'

def main():
    with open(actionsPath) as f:
        schema: dict = json.load(f)
        config = schema['config']
        address = int(config['default_address'], 16) if 'default_address' in config else None
        delay = config['default_delay'] / 1000 if 'default_delay' in config else 0
        busSpeed = config['bus_speed'] if 'bus_speed' in config else 100000
        
        i2c = I2CPico(address, busSpeed)
        
        for step in schema['steps']:
            HandlerFactory(step, i2c, delay)

main()