from configparser import ConfigParser
from pkg_resources import resource_filename

_CONFIG_DISPATCHER = ConfigParser()
_CONFIG_DISPATCHER.read(resource_filename("config", "application.ini"))
_MAIN_PARSER = ConfigParser()
_MAIN_PARSER.read(resource_filename("config", _CONFIG_DISPATCHER["configuration_file"]["active_file"]))

# json sort api info
MYSQL_PORT = float(_MAIN_PARSER["json_sort_api"]["mysql_port"])

