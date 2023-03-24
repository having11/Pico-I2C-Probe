# Pico I2C Probe

An I2C probe based on the Raspberry Pi Pico

- [Pico I2C Probe](#pico-i2c-probe)
  - [What is it?](#what-is-it)
  - [Features](#features)
  - [The interface](#the-interface)
    - [USB](#usb)
    - [JSON](#json)
      - [Sample schema](#sample-schema)
      - [Structure](#structure)
      - [Actions schema](#actions-schema)
        - [Scan](#scan)
        - [Check for device](#check-for-device)
        - [Write data](#write-data)
        - [Read data](#read-data)
        - [Write then read](#write-then-read)
        - [Repeat](#repeat)

## What is it?

The Pico I2C Probe is a simple device meant for testing an I2C bus with various writing, reading, and scanning capabilities

## Features

- Set bus speed
- Scan
- Check for specific address
- Write data
- Read data
- Write then read

## The interface

All I2C communication occurs on pins `GP4 (SDA)`  and `GP5 (SCL)`. Ensure there is a pullup resistor on each of the two lines.

### USB

An interactive, imperative CLI that lets users execute specific actions over USB. :warning: Not implemented!

### JSON

A JSON file with the name of `actions.json` can be dropped to the Pico from a host device which executes each command in order and prints the results to the terminal over USB.

#### Sample schema

```json
{
    "config":
    {
        "bus_speed": 100000,
        "default_address": "0x02",
        "default_delay": 5
    },
    "steps":
    [
        {
            "action": "WRITE",
            "data": [2, 3, 50],
            "delay": 10
        },
        {
            "action": "REPEAT",
            "times": 10,
            "delay": 20,
            "steps":
            [
                {
                    "action": "READ",
                    "bytes_to_read": 1
                },
                {
                    "action": "CHECK_ADDR",
                    "address": "0xa2"
                }
            ]
        },
        {
            "action": "WRITE_THEN_READ",
            "data": [10],
            "bytes_to_read": 1
        },
        {
            "action": "WRITE",
            "address": "0x1f",
            "data": [23, 255]
        }
    ]
}
```

#### Structure

The first key is `config`, and it supports the following keys:

| Key               |   Type   | Default  | Description                                                                                     |
| :---------------- | :------: | :------: | :---------------------------------------------------------------------------------------------- |
| `bus_speed`       | `number` | `100000` | Bus speed in Hz                                                                                 |
| `default_address` | `string` |          | Address of the default address in `HEX`; will be used when `address` not present in an `action` |
| `default_delay`   | `number` |   `0`    | Delay after each `action` in `ms`; will be used when `delay` not present in an `action`         |

The second key is `steps`, and it is an `array` that contains a list of `action`s to perform *sequentially*

#### Actions schema

##### Scan

| Key           |   Type   |    Value    | Optional | Description                                          |
| :------------ | :------: | :---------: | :------: | :--------------------------------------------------- |
| `action`      | `string` |  `"SCAN"`   |    No    | Scan the bus for devices                             |
| `delay`       | `number` | Delay in ms |   Yes    | Delay after action                                   |
| `log_message` | `string` |             |   Yes    | Print message to terminal before execution of action |

##### Check for device

| Key           |   Type   |      Value       | Optional | Description                                          |
| :------------ | :------: | :--------------: | :------: | :--------------------------------------------------- |
| `action`      | `string` |  `"CHECK_ADDR"`  |    No    | See if device exists at address                      |
| `address`     | `string` | Address in `HEX` |   Yes    | Address to check                                     |
| `delay`       | `number` |   Delay in ms    |   Yes    | Delay after action                                   |
| `log_message` | `string` |                  |   Yes    | Print message to terminal before execution of action |

##### Write data

| Key           |        Type         |        Value        | Optional | Description                                          |
| :------------ | :-----------------: | :-----------------: | :------: | :--------------------------------------------------- |
| `action`      |      `string`       |      `"WRITE"`      |    No    | Write bytes to address                               |
| `data`        | `array` of `number` | `[byte, byte, ...]` |    No    | Array of bytes to send                               |
| `address`     |      `string`       |  Address in `HEX`   |   Yes    | Address which receives written data                  |
| `delay`       |      `number`       |     Delay in ms     |   Yes    | Delay after action                                   |
| `log_message` |      `string`       |                     |   Yes    | Print message to terminal before execution of action |

##### Read data

| Key             |   Type   |      Value       | Optional | Description                                          |
| :-------------- | :------: | :--------------: | :------: | :--------------------------------------------------- |
| `action`        | `string` |     `"READ"`     |    No    | Read bytes from address                              |
| `bytes_to_read` | `number` |                  |    No    | Number of bytes the host expects to receive          |
| `address`       | `string` | Address in `HEX` |   Yes    | Address which sends data                             |
| `delay`         | `number` |   Delay in ms    |   Yes    | Delay after action                                   |
| `log_message`   | `string` |                  |   Yes    | Print message to terminal before execution of action |

##### Write then read

| Key             |        Type         |        Value        | Optional | Description                                          |
| :-------------- | :-----------------: | :-----------------: | :------: | :--------------------------------------------------- |
| `action`        |      `string`       | `"WRITE_THEN_READ"` |    No    | Write bytes followed by immediate read from address  |
| `data`          | `array` of `number` | `[byte, byte, ...]` |    No    | Array of bytes to send                               |
| `bytes_to_read` |      `number`       |                     |    No    | Number of bytes the host expects to receive          |
| `address`       |      `string`       |  Address in `HEX`   |   Yes    | Address to check                                     |
| `delay`         |      `number`       |     Delay in ms     |   Yes    | Delay after action                                   |
| `log_message`   |      `string`       |                     |   Yes    | Print message to terminal before execution of action |

##### Repeat

| Key           |        Type         |    Value    | Optional | Description                                          |
| :------------ | :-----------------: | :---------: | :------: | :--------------------------------------------------- |
| `action`      |      `string`       | `"REPEAT"`  |    No    | Repeat the action `n` number of times                |
| `steps`       | `array` of `action` |             |    No    | List of actions to repeat                            |
| `times`       |      `number`       |             |    No    | Number of times to repeat `repeat_action`            |
| `delay`       |      `number`       | Delay in ms |   Yes    | Delay after each action                              |
| `log_message` |      `string`       |             |   Yes    | Print message to terminal before execution of action |
