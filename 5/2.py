# Tis one gives the correct answer

file = "5/input"
minsize=50000

def get_file():
    with open(file, "r") as f:
        pol_str = f.readline()
    return [a for a in pol_str[:-1]]

def compcase(c1, c2):
    if (c1 == 0 or c2 == 0):
        return 0 
    elif ((c1.isupper() != c2.isupper()) and (c1.upper() == c2.upper())):
        return 1
    else:
        return 0

for pchar in "abcdefghijklmnopqrstuvwxyz":
    FLAG=1
    # Reads the characters

    pol = get_file()
    # Remove the characters from the 
    pol = [a for a in pol if (a.upper() != pchar.upper())]

    while(FLAG):
        FLAG=0
        i=0
        for i in range(len(pol[:-1])):
            while(compcase(pol[i], pol[i+1])):
                pol[i] = 0
                pol[i+1] = 0
                FLAG=1
            i+=1

        pol = [a for a in pol if a != 0]

    if len(pol) < minsize:
        min_probchar = pchar
        min_pol = pol
        minsize=len(pol)
    

print(min_probchar)
print(min_pol)
minsize

