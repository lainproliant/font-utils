#!/usr/bin/env python3
import os
import pathlib
import json
import shlex
import subprocess
import textwrap


# -------------------------------------------------------------------
CONFIG_FILE = pathlib.Path('./config.json')


# -------------------------------------------------------------------
def list_fonts():
    return subprocess.check_output("./list-monospace-fonts.sh").decode("utf-8").split("\n")


# -------------------------------------------------------------------
def load_config():
    with open(CONFIG_FILE.name, 'r') as infile:
        return json.load(infile)


# -------------------------------------------------------------------
def save_config(config):
    with open(CONFIG_FILE.name, 'w') as outfile:
        json.dump(config, outfile)


# -------------------------------------------------------------------
def main():
    fonts = list_fonts()

    try:
        config = load_config()
    except FileNotFoundError:
        config = {
            'font': fonts[0],
            'size': 14
        }

    try:
        index = fonts.index(config['font'])
    except ValueError:
        index = -1

    while True:
        inp = input(f"{config['font']}:{config['size']} > ")
        if not inp:
            continue

        cmd, *args = shlex.split(inp)

        if "exit".startswith(cmd) or 'quit'.startswith(cmd):
            break

        if "next".startswith(cmd):
            index += 1
            if index >= len(fonts):
                index = 0
            config['font'] = fonts[index]
            save_config(config)
            subprocess.call(["./apply.sh"])

        elif "prev".startswith(cmd):
            index -= 1
            if index < 0:
                index = 0
            config['font'] = fonts[index]
            save_config(config)
            subprocess.call(["./apply.sh"])

        elif "all".startswith(cmd):
            os.system('./list-all-fonts.sh | less')

        elif "list".startswith(cmd):
            os.system('./list-monospace-fonts.sh | less')

        elif "clear".startswith(cmd):
            os.system('clear')

        elif "override".startswith(cmd):
            if not args:
                print('Missing font argument.')
                continue
            try:
                index = fonts.index(args[0])
                config['font'] = fonts[index]
            except ValueError:
                index = -1
                config['font'] = args[0]

            save_config(config)
            subprocess.call(["./apply.sh"])

        elif "font".startswith(cmd):
            if not args:
                print('Missing font argument.')
                continue
            try:
                index = fonts.index(args[0])
                config['font'] = fonts[index]
                save_config(config)
                subprocess.call(["./apply.sh"])
            except ValueError:
                print(f"Font '{args[0]}' doesn't exist.")

        elif "size".startswith(cmd):
            config['size'] = int(args[0])
            save_config(config)
            subprocess.call(["./apply.sh"])

    save_config(config)


# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
