from config_parser import ConfigParser



Maze_config = ConfigParser("config.txt")
# Maze_config.parse_config()
print(Maze_config.config)
# print(Maze_config.get_value("WIDTH"))