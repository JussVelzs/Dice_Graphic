import random

def dicepy():
    possible_outcomes = ["1", "2", "3", "4", "5", "6"]
    outcome = possible_outcomes[random.randint(0, 5)]
    print(outcome)
    ###
    if outcome == "1":
        print("""
    -------------
    |   |   |   |
    |---+---+---|
    |   | 0 |   |
    |---+---+---|
    |   |   |   |
    -------------
    """)
    elif outcome == "2":
        print("""
    -------------
    |   |   | 0 |
    |---+---+---|
    |   |   |   |
    |---+---+---|
    | 0 |   |   |
    -------------
    """)
    elif outcome == "3":
        print("""
    -------------
    |   |   | 0 |
    |---+---+---|
    |   | 0 |   |
    |---+---+---|
    | 0 |   |   |
    -------------
    """)
    elif outcome == "4":
        print("""
    -------------
    | 0 |   | 0 |
    |---+---+---|
    |   |   |   |
    |---+---+---|
    | 0 |   | 0 |
    -------------
    """)
    elif outcome == "5":
        print("""
    -------------
    | 0 |   | 0 |
    |---+---+---|
    |   | 0 |   |
    |---+---+---|
    | 0 |   | 0 |
    -------------
    """)
    else:
        print("""
    -------------
    | 0 |   | 0 |
    |---+---+---|
    | 0 |   | 0 |
    |---+---+---|
    | 0 |   | 0 |
    -------------
    """)



dicepy()
