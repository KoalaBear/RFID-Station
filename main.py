import argparse

import station_cli
import station_gui


class Sensor:
    CURRENT_CODE = ""

    @staticmethod
    def write(status_text=None):
        Sensor._write_rfid()
        print(f"[WROTE]: {Sensor.CURRENT_CODE}..")
        if status_text:
            status_text.config(text=f"[WROTE]: {Sensor.CURRENT_CODE}")

    @staticmethod
    def read(text_label=None):
        code_read = Sensor._read_rfid()
        Sensor.CURRENT_CODE = code_read
        print(f"[READ]: {code_read}")
        if text_label:
            text_label.config(text=code_read)

    @staticmethod
    def _read_rfid():
        return 2  # TODO

    @staticmethod
    def _write_rfid():
        pass  # TODO


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--cli', action='store_true', default=False)
    flags = p.parse_args()
    if flags.cli:
        station_cli.start()
    station_gui.start()
