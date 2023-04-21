import sys

red = 1 
reds = [red,red,red,red,red,red,red,red,red,red,red,red,red,red,red]
colours = {
    "yellow": 2,
    "green":  3,
    "brown":  4,
    "blue":   5,
    "pink":   6,
    "black":  7
    }

def calc_max(detail="n"):
    total = 0
    # Calc value after potting all red balls with the black ball
    for x in reds:
        total = total + (x + colours.get("black"))    
    # Calc value after potting all coloured balls 
    total = total + calc_colours()
    print("Highest possible score:", total)
    if detail != "n":
        print("\nThis score is only possible if the player pots a black ball for every red ball they potted AND pots all colours in the final stage of the set.")
        
def calc_colours():
    total = 0
    for x in colours.keys():
        total = total + colours[x]
    return total

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])