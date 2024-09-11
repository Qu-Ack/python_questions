str = "this is a test"


def n_endswith(character, str):
    if str[-1] == character:
        return True
    else:
        return False


print(n_endswith("e", str))
