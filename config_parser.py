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
                'OUTPUT_FILE':  None,
                'PERFECT':      None,
        }

    '''Get config file data and save config'''
    def parse_config(self) -> None:
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()

                    # Skip empty and comment
                    if not line or line.startswith("#"):
                        continue

                    # Partition the line with "="
                    key, _, value = line.partition("=")

                    # Check if key is valid or not
                    if key not in self.config:
                        print("Error: Invalid key")
                        sys.exit(1)
                    else:
                        self.config[key.strip()] = value.strip()
            
            #Validate and casting config data
            self.check_valid_data()

            # Check missing value
            for key, value in self.config.items():
                if value is None:
                    print(f"Missing {key} in config")
                    sys.exit(1)
        except OSError as e:
            print (f"OS ERROR! {e}")
        except Exception as e:
            print(f"ERROR! {e}")
            sys.exit(1)

    '''Validate and casting config data'''
    def check_valid_data(self) -> None:
            # 1.Check dimension values
            for key, val in self.config.items():
                try:
                    if key == "WIDTH":
                        if (int(val) < 0):
                            print("ERROR!: WIDTH value must be >= 0")
                            sys.exit(1)
                        self.config.update({key: int(val)})
                    if key == "HEIGHT":
                        if (int(val) < 0):
                            print("ERROR!: HEIGHT value must be >= 0")
                            sys.exit(1)
                        self.config.update({key: int(val)})
                except ValueError as e:
                    print(f"ERROR! {e}")
            
            # 2.Check ENTRY AND EXIT values
            for key, val in self.config.items():
                try:
                    if key == "ENTRY" or key == "EXIT":
                        coordinates = val.split(',')
                        if len(coordinates) != 2:
                            print("ERROR! Invalid ENTRY/EXIT input")
                            sys.exit(1)
                        x, y = int(coordinates[0]), int(coordinates[1])
                    width, height = self.config["width"], self.config["height"]
                    if x < 0 or x >= width:
                        print("ERROR! Invalid ENTRY/EXIT input")
                    if y < 0 or y >= height:
                        print("ERROR! Invalid ENTRY/EXIT input")
                    self.config.update({key, (int(x), int(y))})
                except ValueError as e:
                    print(f"ERROR! {e}")

            # 3. Check PERFECT bool value
            for key, val in self.config.items():
                if key == "PERFECT":
                    if val == "True" or "1":
                        self.config[key] = True
                    elif val == "False" or "0":
                        self.config[key] = False
    
    '''Get maze config data'''
    def get_value(
        self,
        data_name: str
        ) -> int | str | dict[str, int] | None:
        return self.config.get(data_name)

