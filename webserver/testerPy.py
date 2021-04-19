
def switch(argument):
    switcher = {
        'N/A': 0,
        'Iron': 1,
        'Bronze': 2,
        'Silver': 3,
        'Gold': 4,
        'Platinum': 5,
        'Diamond': 6,
        'Master': 7,
        'Grandmaster': 8,
        'Challenger': 9
    }
    return switcher.get(argument, "nothing")

print(switch('Master'))