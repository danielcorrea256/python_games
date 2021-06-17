NAME_FILE = "max_score.txt"

def get_max_score():
    with open(NAME_FILE, "r") as f:
        lines = f.readlines()
        score = lines[0].strip()
    return score


def update_max_score(new_score):
    max_score = get_max_score()
    with open(NAME_FILE, "w") as f:
        if int(new_score) > int(max_score):
            f.write(str(new_score))
        else:
            f.write(max_score)
