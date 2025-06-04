# ELD-Test-Tool

This repository contains utilities for testing Electronic Logging Device (ELD) functionality.

## UART Connection Script

`connect_uart.py` allows you to connect to a UART serial port from the command line.

### Requirements

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Usage

Run the script with the desired port and baud rate:

```bash
python connect_uart.py -p COM3 -b 115200
```

Replace `COM3` with the appropriate port name on your system (e.g. `/dev/ttyUSB0` on Linux).
