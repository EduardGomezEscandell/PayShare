import pay_share
import sys

# Defaults
file_name = "tests/data/long_sample.tsb"
language = "en"

# Input parsing
if len(sys.argv) > 1:
    file_name = sys.argv[1]
if len(sys.argv) > 2:
    language = sys.argv[2]
if len(sys.argv) > 3:
    raise RuntimeError("Unrecognized input. Please write:\n    python example.py <file_name.tsb> <language>")

# Seting language
pay_share.Localization.set(language)

# Reading from file
pay_share.Currency.symbol = "EUR"
book = pay_share.Book()
reader = pay_share.LogReader(book, file_name)
book.load_from_file(reader)

# Computing
book.compute_corrections()

# Printing results
for agent in book.agents.values():
    print("-------------------------------------")
    print(agent.report())

print("\n-------------------------------------")
print(book.report())