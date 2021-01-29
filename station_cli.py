from main import Sensor

INPUT_SUFFIX = "\n\t> "
PRINT_WARNING = '\033[93m'
PRINT_RESET = '\033[0m'


def start():
    while True:
        print(f"\n\n~~~~ CURRENT CODE: '{Sensor.CURRENT_CODE}' ~~~~")
        options = {"r": Sensor.read, "w": Sensor.write, "e": lambda: exit(0)}
        handle_cmd(cli_input(f"Would you like to [R]ead, [W]rite or [E]xit?", options.keys()), options)


def handle_cmd(cmd, options):
    options[cmd]()


def cli_input(instruction, valid_values):
    cmd = input(f"{instruction}{INPUT_SUFFIX}").lower()
    while cmd not in valid_values:
        print(PRINT_WARNING, "\n/** Invalid Input **\\\n", PRINT_RESET)
        cmd = input(f"{instruction}{INPUT_SUFFIX}").lower()
    return cmd
