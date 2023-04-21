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

def calc_max():
    total = 0
    for x in reds:
        total = total + (x + colours.get("black"))    
    total = total + calc_colours()
    print(total)
        
def calc_colours():
    total = 0
    for x in colours.keys():
        total = total + colours[x]
    return total

if __name__ == '__main__':
    globals()[sys.argv[1]]()