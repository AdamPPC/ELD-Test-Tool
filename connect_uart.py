import argparse
import serial


def main():
    parser = argparse.ArgumentParser(description="Connect to a UART COM port")
    parser.add_argument('-p', '--port', required=True, help='Serial port name, e.g. COM3 or /dev/ttyUSB0')
    parser.add_argument('-b', '--baudrate', type=int, default=9600, help='Baud rate (default: 9600)')
    args = parser.parse_args()

    try:
        with serial.Serial(args.port, args.baudrate, timeout=1) as ser:
            print(f"Connected to {args.port} at {args.baudrate} baud.")
            print("Press Ctrl+C to exit.")
            while True:
                if ser.in_waiting:
                    data = ser.read(ser.in_waiting)
                    print(data.decode(errors='replace'), end='')
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nDisconnected.")


if __name__ == '__main__':
    main()
