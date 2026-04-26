"""
main.py
Entry point for the Gas & Air Quality Monitor Dashboard.

Usage:
    python main.py                   # runs with simulated data (demo mode)
    python main.py --port COM3       # connects to real Arduino on COM3
    python main.py --port /dev/ttyUSB0  # Linux/macOS Arduino port
"""

import argparse
from sensor import SensorSimulator, ArduinoSensor
from logger import DataLogger
from dashboard import Dashboard


def main():
    parser = argparse.ArgumentParser(description="Gas & Air Quality Monitor")
    parser.add_argument("--port", type=str, default=None,
                        help="Serial port for Arduino (e.g. COM3 or /dev/ttyUSB0). "
                             "Omit to run in simulation mode.")
    parser.add_argument("--baud", type=int, default=9600,
                        help="Baud rate (default: 9600)")
    args = parser.parse_args()

    # ── Choose sensor source ──────────────────────────────────────────────────
    if args.port:
        print(f"[Main] Connecting to Arduino on {args.port} @ {args.baud} baud...")
        sensor = ArduinoSensor(port=args.port, baud=args.baud)
    else:
        print("[Main] No port specified — running in SIMULATION mode.")
        sensor = SensorSimulator()

    logger    = DataLogger()
    dashboard = Dashboard(sensor, logger)
    dashboard.run()


if __name__ == "__main__":
    main()