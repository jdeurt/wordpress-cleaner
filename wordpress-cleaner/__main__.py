import core
import configparser
import re
import os

config = configparser.ConfigParser()
config.read("config.txt")

root_dir = os.path.realpath(os.path.normpath(config["files"]["root_dir"]))
malware_regexp_compiled = re.compile(config["files"]["malware_regex"])
file_extensions = config["files"]["file_extensions"].split(",")

core.clean_files(root_dir, malware_regexp_compiled, file_extensions)