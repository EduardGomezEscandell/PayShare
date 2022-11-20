import sys

file = __file__.replace('\\','/')

source_folder = "/".join(file.split('/')[:-1]) + "/source"
sys.path.append(source_folder)

localization_folder = "/".join(file.split('/')[:-1]) + "/localization"
sys.path.append(localization_folder)

from source.agent import Agent as Agent
from source.book import Book as Book
from source.currency import Currency as Currency
from source.log_reader import LogReader as LogReader
from source.operation import Operation as Operation
from source.localization import Localization as Localization
