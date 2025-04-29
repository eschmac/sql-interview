from impl.sql import SQL

import pytest

def test_sql_example_1():
    s = SQL(["one", "two", "three"], [2, 3, 1]) # Creates three tables.

    outputs = []

    # Adds a row to the table "two" with id 1. Returns True.
    outputs.append(s.ins("two", ["first", "second", "third"])) 

    # Returns the value "third" from the third column
    # in the row with id 1 of the table "two".
    outputs.append(s.sel("two", 1, 3))

    # Adds another row to the table "two" with id 2. Returns True.
    outputs.append(s.ins("two", ["fourth", "fifth", "sixth"]))

    # Exports the rows of the table "two".
    # Currently, the table has 2 rows with ids 1 and 2.
    outputs.append(s.exp("two"))

    # Removes the first row of the table "two". Note that the second row
    # will still have the id 2.
    outputs.append(s.rmv("two", 1))

    # Returns the value "fifth" from the second column
    # in the row with id 2 of the table "two".
    outputs.append(s.sel("two", 2, 2))

    # Exports the rows of the table "two".
    # Currently, the table has 1 row with id 2.
    outputs.append(s.exp("two"))
    
    expected_outputs = [True,"third",True,["1,first,second,third","2,fourth,fifth,sixth"],None,"fifth",["2,fourth,fifth,sixth"]]
    for i, o in enumerate(outputs):
        if o != expected_outputs[i]:
            pytest.fail(f"step {i} should've returned {expected_outputs[i]} but returned {o}")