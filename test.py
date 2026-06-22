from config_parser import ConfigParser

Maze_config = ConfigParser("config.txt")
Maze_config.parse_config()
Maze_config.check_valid_data()
for key,val in Maze_config.config.items():
    print(f"{key} : {val}")
print (Maze_config.get_value("WIDTH"))
# print(Maze_config.get_value("WIDTH"))