#!/usr/bin/env python3
import sys
from typing import Any
import str


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
            with open(filename, "r") as f:
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
            
            # Check missing value
            for key, value in self.config.items():
                if value is None:
        except Exception as e:
            print(f"ERROR! {e}")
            sys.exit(1)

    '''Checking each config data'''





        



