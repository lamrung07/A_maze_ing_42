#!/usr/bin/env python3
import sys
from typing import Any


# -----------------------------------------------
# Config parser main class
# -----------------------------------------------

class ConfigParser:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.config: dict[str, Any] = {
                'WIDTH':        None,
                'HEIGHT':       None,
                'ENTRY':        None,
                'EXIT':         None,
                'SEED':         None,
                'OUTPUT_FILE':  None,
                'PERFECT':      None,
        }

    def parse_config(self) -> None:
        """Get config file data and save config"""

        # Parsing raw data from config file
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()

                    # Skip empty and comment
                    if not line or line[0] == "#":
                        continue

                    # Partition the line with "="
                    key, _, value = line.partition("=")

                    # Check if key is valid or not
                    if key not in self.config:
                        print(f"Error!: Invalid key '{key}'")
                        sys.exit(1)
                    else:
                        self.config[key.strip()] = value.strip()

            # Check missing value
            for key, value in self.config.items():
                if value is None:
                    print(f"Missing {key} in config")
                    sys.exit(1)

        except OSError as e:
            print(f"OS ERROR! {e}")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR! {e}")
            sys.exit(1)

    def check_valid_data(self) -> None:
        """Validate and casting config data"""
        # 1.Check dimension values
        try:
            key, val = "WIDTH", self.config["WIDTH"]
            if (int(val) < 0):
                print("ERROR!: WIDTH value must be >= 0")
                sys.exit(1)
            self.config[key] = int(val)
            key, val = "HEIGHT", self.config["HEIGHT"]
            if (int(val) < 0):
                print("ERROR!: HEIGHT value must be >= 0")
                sys.exit(1)
            self.config[key] = int(val)
        except ValueError as e:
            print(f"ERROR! {e}")
            sys.exit(1)

        # 2.Check ENTRY AND EXIT values
        try:
            x, y = 0, 0
            width = self.config["WIDTH"]
            height = self.config["HEIGHT"]

            # Check ENTRY value
            key, val = "ENTRY", self.config["ENTRY"]
            coordinates = val.split(',')
            if len(coordinates) != 2:
                print("ERROR! Invalid ENTRY input")
                sys.exit(1)
            x, y = int(coordinates[0]), int(coordinates[1])
            if x < 0 or x >= width:
                print("ERROR! Invalid ENTRY input")
                sys.exit(1)
            if y < 0 or y >= height:
                print("ERROR! Invalid ENTRY input")
                sys.exit(1)
            self.config[key] = (int(x), int(y))

            # Check EXIT value
            key, val = "EXIT", self.config["EXIT"]
            coordinates = val.split(',')
            if len(coordinates) != 2:
                print("ERROR! Invalid EXIT input")
                sys.exit(1)
            x, y = int(coordinates[0]), int(coordinates[1])
            if x < 0 or x >= width:
                print("ERROR! Invalid EXIT input")
                sys.exit(1)
            if y < 0 or y >= height:
                print("ERROR! Invalid EXIT input")
                sys.exit(1)
            self.config[key] = (int(x), int(y))

            # 3. Check SEED value
            key, val = "SEED", self.config["SEED"]
            coordinates = val.split(',')
            if len(coordinates) != 2:
                print("ERROR! Invalid SEED input")
                sys.exit(1)
            x, y = int(coordinates[0]), int(coordinates[1])
            if x < 0 or x >= width:
                print("ERROR! Invalid SEED input")
                sys.exit(1)
            if y < 0 or y >= height:
                print("ERROR! Invalid SEED input")
                sys.exit(1)
            self.config[key] = (int(x), int(y))

        except ValueError as e:
            print(f"ERROR! {e}")
            sys.exit(1)

            # 4. Check PERFECT bool value
            for key, val in self.config.items():
                if key == "PERFECT":
                    if val == "True" or "1":
                        self.config[key] = True
                    elif val == "False" or "0":
                        self.config[key] = False

    def get_value(
        self,
        data_name: str
    ) -> int | str | dict[str, int] | None:
        """Get maze config data"""
        return self.config.get(data_name)
