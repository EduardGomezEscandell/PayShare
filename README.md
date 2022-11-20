# PayShare

This python program helps settle debt after a group activity. Give it the list of operations, who payed and who enjoyed them, and the program will tell you who should pay whom and why.

## How to run
You can create your own script but `example.py` is ready to go. If ran as:

`python example.py`

a sample will be run. If you want to use your own data, you must run:

`python example.py path/to/my/file.tsb`

The data input format is explained in the next section. The output will have a report for each person (so you can mail it to the person directly), plus a summary report with all operations.

## Input and output
The data input is a tab-separated-value file with the format:
- Lines starting with # are ignored
- Empty lines are not allowed
- Each non-ignored line is a distinct operation
- There must be at least 3 colums:
    - Payer name.
    - Consumer names (separated by commas, non-tab whitespace is ignored).
    - Value of the transaction.
    - All remaining columns (if any) will be considered part of the description.

An example line might be:

```Alice	Alice, Bob, Eve	19.50	Last thurday's coffees```

This would generate the following report:
```
>> python .\example.py alice_and_bob.tsb
-------------------------------------
Report for Alice

You have payed for the following operations:
     19.50 EUR : Last thurday's coffees
You have benefited from the following operations:
      6.50 EUR : Last thurday's coffees
This results in a balance of 13.00 EUR

In order to set the balance to zero you will pay:
  (nothing)
and you will receive:
      6.50 EUR from Eve
      6.50 EUR from Bob

-------------------------------------
Report for Bob

You have payed for the following operations:
  (nothing)
You have benefited from the following operations:
      6.50 EUR : Last thurday's coffees
This results in a balance of -6.50 EUR

In order to set the balance to zero you will pay:
      6.50 EUR to Alice
and you will receive:
  (nothing)

-------------------------------------
Report for Eve

You have payed for the following operations:
  (nothing)
You have benefited from the following operations:
      6.50 EUR : Last thurday's coffees
This results in a balance of -6.50 EUR

In order to set the balance to zero you will pay:
      6.50 EUR to Alice
and you will receive:
  (nothing)


-------------- SUMMARY --------------
The following operations took place:
     19.50 EUR  Alice -> Alice, Bob, Eve : Last thurday's coffees

In order to set the balance to zero, the following payments must take place:
      6.50 EUR  Eve -> Alice
      6.50 EUR  Bob -> Alice

```

## Language
You can select the language by adding a second argument if using `example.py`:
```
python example.py path/to/file.tsb es
```
The current list of languages and their labels are:
- `en`: English
- `es`: Spanish
- `ca`: Catalan

The following elements are not translated:
- Error messgaes and exceptions
- Operation descriptions: they are displayed in the language you write them in the `tsb` file.
