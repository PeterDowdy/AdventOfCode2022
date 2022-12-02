data = []
with open("day2.txt") as f:
    data = [x.strip() for x in f.readlines()]

theirs = {"A": "rock", "B": "paper", "C": "scissors"}

scores = {"rock": 1, "paper": 2, "scissors": 3}

score = 0
for combo in data:
    their_symbol, my_symbol = combo.split()
    their_thing = theirs[their_symbol]
    my_thing = None
    if my_symbol == "X":
        my_thing = (
            "rock"
            if their_thing == "paper"
            else "scissors"
            if their_thing == "rock"
            else "paper"
            if their_thing == "scissors"
            else None
        )
    elif my_symbol == "Y":
        my_thing = their_thing
    elif my_symbol == "Z":
        my_thing = (
            "rock"
            if their_thing == "scissors"
            else "paper"
            if their_thing == "rock"
            else "scissors"
            if their_thing == "paper"
            else None
        )
    base_score = scores[my_thing]
    if their_thing == my_thing:
        score += base_score + 3
    elif (
        (their_thing == "rock" and my_thing == "scissors")
        or (their_thing == "paper" and my_thing == "rock")
        or (their_thing == "scissors" and my_thing == "paper")
    ):
        score += base_score
    elif (
        (their_thing == "scissors" and my_thing == "rock")
        or (their_thing == "rock" and my_thing == "paper")
        or (their_thing == "paper" and my_thing == "scissors")
    ):
        score += base_score + 6

print(score)
