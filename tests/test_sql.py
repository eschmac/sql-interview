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

def test_sql_example_2():
    s = SQL(["one", "two", "three"], [2, 3, 1]) # Creates three tables.

    outputs = []

    # Adds a row to the table "two" with id 1. Returns True. 
    outputs.append(s.ins("two", ["first", "second", "third"]))

    # Returns the value "third" from the third column 
    # in the row with id 1 of the table "two".
    outputs.append(s.sel("two", 1, 3))

    # Removes the first row of the table "two".
    outputs.append(s.rmv("two", 1))

    # Returns "<null>" as the cell with id 1 
    # has been removed from table "two".
    outputs.append(s.sel("two", 1, 2))

    # Returns False as number of columns are not correct.
    outputs.append(s.ins("two", ["fourth", "fifth"]))

    # Adds a row to the table "two" with id 2. Returns True.
    outputs.append(s.ins("two", ["fourth", "fifth", "sixth"]))
    
    expected_outputs = [True,"third",None,"<null>",False,True]
    for i, o in enumerate(outputs):
        if o != expected_outputs[i]:
            pytest.fail(f"step {i} should've returned {expected_outputs[i]} but returned {o}")

def test_example_3():
    s = SQL(["ez","v","u","pl","rz","snlw","qk","egy","x","iyzdq","bpfef","vr"],[7,8,2,3,5,5,2,6,4,1,1,5])
    
    calls = ["ins","sel","sel","sel","sel","ins","sel","ins","ins","rmv","sel","ins","sel","sel","sel","sel","rmv","sel","sel","sel","ins","rmv","sel","sel","sel","sel","ins","ins","sel","ins","sel","ins","sel","sel","rmv","ins","ins","sel","ins","sel","sel","sel","ins","sel","sel","ins","sel","rmv","sel","sel","rmv","rmv","ins","sel","sel","sel","sel","sel","sel","rmv","ins","rmv","sel","sel","rmv","sel","rmv","ins","sel","rmv","ins","sel","sel","sel","ins","rmv"]
    inputs = [["u",["lae","l"]],["u",1,2],["u",1,2],["u",1,2],["u",1,1],["ez",["kkn","dka","xrij","li","cc","g","f"]],["ez",1,5],["iyzdq",["lo"]],["vr",["y","i","f","ll","mps"]],["vr",1],["iyzdq",1,1],["qk",["lu","jeazw"]],["ez",1,6],["qk",1,1],["u",1,1],["u",1,1],["ez",1],["iyzdq",1,1],["iyzdq",1,1],["u",1,2],["bpfef",["kz"]],["iyzdq",1],["qk",1,1],["u",1,1],["qk",1,2],["u",1,2],["iyzdq",["cu"]],["x",["nrnet","fiy","pbmp","tbgs"]],["x",1,2],["iyzdq",["t"]],["iyzdq",3,1],["egy",["lg","pmtu","joqdt","psdyy","nk","gfb"]],["bpfef",1,1],["bpfef",1,1],["egy",1],["snlw",["jbu","s","xeuqs","zvvy","izogr"]],["rz",["vodbu","bpd","pa","eu","eu"]],["iyzdq",2,1],["qk",["kbjqg","y"]],["qk",2,2],["rz",1,5],["qk",1,1],["iyzdq",["hlujc"]],["rz",1,3],["iyzdq",3,1],["rz",["vw","yq","imkyf","bpv","kfne"]],["rz",1,1],["x",1],["rz",2,1],["qk",2,1],["qk",1],["iyzdq",2],["rz",["wdvcr","vpb","a","ar","xvbl"]],["rz",1,4],["iyzdq",4,1],["rz",2,4],["bpfef",1,1],["snlw",1,2],["bpfef",1,1],["rz",3],["vr",["it","tr","bgia","b","zif"]],["iyzdq",4],["bpfef",1,1],["vr",2,1],["iyzdq",3],["vr",2,3],["qk",2],["v",["onmdi","noe","sv","slyt","ruv","iscm","r","spti"]],["rz",1,3],["vr",2],["iyzdq",["ewkky"]],["rz",2,1],["iyzdq",5,1],["rz",2,4],["x",["g","zkp","skj","xng"]],["iyzdq",5]]
    translations = {
        "ins": s.ins,
        "sel": s.sel,
        "rmv": s.rmv, 
        "exp": s.exp,
    }
    
    outputs = []
    for i, call in enumerate(calls):
        f = translations[call]
        outputs.append(f(*inputs[i]))
        
    expected_outputs = [True,"l","l","l","lae",True,"cc",True,True,None,"lo",True,"g","lu","lae","lae",None,"lo","lo","l",True,None,"lu","lae","jeazw","l",True,True,"fiy",True,"t",True,"kz","kz",None,True,True,"cu",True,"y","eu","lu",True,"pa","t",True,"vodbu",None,"vw","kbjqg",None,None,True,"eu","hlujc","bpv","kz","s","kz",None,True,None,"kz","it",None,"bgia",None,True,"pa",None,True,"vw","ewkky","bpv",True,None]
    for i, o in enumerate(outputs):
        if o != expected_outputs[i]:
            pytest.fail(f"step {i} should've returned {expected_outputs[i]} but returned {o}")