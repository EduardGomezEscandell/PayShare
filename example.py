import pay_share
import sys

# Input parsing
if len(sys.argv) == 1:
    file_name = "tests/data/long_sample.tsb"
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    raise RuntimeError("Unrecognized input. Please write:\n    python example.py file_name.tsb")

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

print("\n-------------- SUMMARY --------------")
print(book.report())