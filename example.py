#!/bin/python3
"""
This example program shows how to use payshare in order to settle
debts after a group activity.
"""

import sys
import payshare

# Defaults
DEFAULT_FILENAME = "tests/data/long_sample.tsb"
DEFAULT_LANGUAGE = ""

# Input parsing
if len(sys.argv) > 1:
    DEFAULT_FILENAME = sys.argv[1]
if len(sys.argv) > 2:
    DEFAULT_LANGUAGE = sys.argv[2]
if len(sys.argv) > 3:
    print("""Unrecognized input. Please write:
python example.py <file_name.tsb> <language>""")
    sys.exit(1)

# Seting language
locale = payshare.Localization(DEFAULT_LANGUAGE)

# Reading from file
payshare.Currency.symbol = "EUR"
book = payshare.Book()
reader = payshare.LogReader(book, DEFAULT_FILENAME)
book.load_from_file(reader)

# Computing
book.compute_corrections()

# Printing results
for agent in book.agents.values():
    print("-------------------------------------")
    print(agent.report(locale))

print("\n-------------------------------------")
print(book.report(locale))
