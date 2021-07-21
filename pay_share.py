import source

import sys, os

file = __file__.replace('\\','/')

source_folder = "/".join(file.split('/')[:-1]) + "/source"
sys.path.append(source_folder)

localization_folder = "/".join(file.split('/')[:-1]) + "/localization"
sys.path.append(localization_folder)

from agent import Agent
from book import Book
from currency import Currency
from log_reader import LogReader
from operation import Operation
from localization import Localization

print("")
print("Imported PayShare")
print("Visit https://github.com/EduardGomezEscandell/PayShare")
print("")