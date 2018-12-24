class unit:
    def __init__(self, x, y, t):
        self.hp = 200
        self.atack = 3
        self.x = x
        self.y = y
        self.t = t   # E or G
        self.alive = 1

    def turn(self, m, unit_list):
        ''' Acts one turn '''

        # Check if there is an adjacent enemy 
        adj_flag, target_x, target_y = self.check_adjacent(unit_list)
        if adj_flag:
            # Atack 
            self.attack(target_x, target_y)
        # No target in range
        else:

            # Get All enemy positions

            while 1:
                # Get the closest one
                # Try to find path
                # If success: break
                break

        # Move one step

    def find_path(self, target_x, target_y, m):
        pass

    def check_adjacent(self, unit_list):
        ''' Determines if atacks or moves ''' 
        # Get coordinates


    def get_enemies(self):
        ''' Gets list of enemies '''
        pass

    def defend(self, atack):
        pass
        
    def attack(self, target_x, target_y):
        pass

# Open File
file = "15/input"
file = "15/test-input"
m = []
with open(file, "r") as f:
    for line in f.readlines():
        m.append(line.strip())
    
def create_units(m: list) -> list:
    ''' Return dict with units,  and replace map with stuff'''
    # Unit Dict
    units = {}
    n_unit = 1

    # Create all units
    for y, line in enumerate(m):
        for x, char in enumerate(line):
            if char in ["E", "G"]:
                # Found a unit
                units[n_unit] = unit(x, y, char)
                n_unit += 1

    # Delete all units from the list
    for i in range(len(m)):
        m[i] = m[i].replace("G", ".")
        m[i] = m[i].replace("E", ".")

    return m, units
    

order = lambda u: (u[1])
def order_units(units: dict) -> dict:
    ''' Orders the units by order '''

    sorted_list = sorted([(k, (val.x, val.y)) for k, val in units.items()], key = order)
    return dict(zip([k for k in range(1, len(units)+1)], [unit[1] for unit in sorted_list]))

def print_units_position(units=units):
    ''' Just for debug '''
    print(sorted([(k, (val.x, val.y)) for k, val in units.items()]))

def end_battle(units):
    ''' End battle if only enemies from one type exist '''

    if len(set([unit.t for unit in units.values()])) > 1:
        return 1
    else: 
        return 0

def run_battle(m, units) -> None:
    ''' Runs part 1 '''

    while end_battle:
        units = order_units(units)

        for unit in units.values():
            unit.turn(m, units)
            

# Solve Part 1
m, units = create_units(m)
run_battle(m, units)
