import numpy as np

class Unit:
    def __init__(self, x, y, t):
        self.hp = 200
        self.atack = 3
        self.x = x
        self.y = y
        self.t = t   # E or G
        self.alive = 1

    def turn(self, m, unit_list, walls):
        ''' Acts one turn '''

        # Get enemy coordinates list:
        enemies_list = [(k, (val.x, val.y))
                        for k, val in unit_list.items()
                        if val.t != self.t and val.alive]

        print("Enemies: ", enemies_list)

        # Check if there is an adjacent enemy 
        enemy = self.check_adjacent(enemies_list)
        if enemy:
            self.attack(enemy)
        # No target in range
        else:
            self.x, self.y = dijkstra(self,
                                      [c for _, c in enemies_list],
                                      unit_list,
                                      walls,
                                      m)

        # Check if there is an adjacent enemy again
        enemy = self.check_adjacent(enemies_list)
        if enemy:
            self.attack(enemy)

    def check_adjacent(self, enemies_list):
        ''' Determines if atacks or moves ''' 
        # Get Adjacent coordinates
        adj = (self.x + 1, self.y,
               self.x, self.y - 1,
               self.x - 1, self.y,
               self.x, self.y + 1)

        attack_enemy = None
        lowest_hp = 200
        # Select enemy with the fewest health points
        for enemy, coords in enemies_list:
            if coords in adj:
                if unit_list[enemy].hp < lowest_hp:
                    lowest_hp = unit_list[enemy].hp
                    atack_enemy = enemy

        return attack_enemy
                    
    def defend(self):
        self.hp -= 3

        if self.hp <= 0:
            self.alive = False

    def attack(self, target):
        unit_list[target].defend()


# Open File
file = "input"
file = "test-input2"
m = []
with open(file, "r") as f:
    for line in f.readlines():
        m.append(line.strip())

# Function to solve the current path
def dijkstra(current_unit, targets, units, walls, m):
    ''' Returns the next step to the shortest path '''

    global graph

    init = current_unit.x, current_unit.y

    # Get List of friendly units (excluding the current)
    list_units = [(val.x, val.y)
                  for val in units.values()
                  if ((val.x, val.y) != init and val.t == current_unit.t and val.alive)
    ]

    # Create list of unvisited coordinates
    # Remove walls and units
    map_w = len(m[0])
    map_h = len(m)

    # Create Grid
    graph = np.full((map_h, map_w), np.inf)

    # Fill unavailable squares with -1
    for x, y in walls + list_units:
        graph[y, x] = -1

    # Create array to store the coordinates of the available nodes
    # All nodes that start with inf
    inf_x, inf_y = np.where(graph != -1)
    coord_list = [(y, x) for x, y in zip(inf_x, inf_y)]

    # Set initial node to 0
    graph[init[1], init[0]] = 0
    graph, coord_list = solve_graph(graph,
                                    [(init[0], init[1])],
                                    coord_list)

    # Get shortest target
    min_d = np.inf
    for x, y in targets:
        if graph[y, x] < min_d:
            min_d = graph[y, x]
            tx, ty = x, y
    print("Shortest Target: ", tx, ty)

    # Get the new_x, new_y
    while graph[ty, tx] != 1:
        min_d = np.inf
        for ny, nx in ((ty+1, tx), (ty, tx+1), (ty-1, tx), (ty, tx-1)):
            try:
                if ny >= 0 and nx >= 0 and graph[ny, nx] < min_d and graph[ny, nx] != -1:
                    min_d = graph[ny, nx]
                    miny, minx = ny, nx
            except: pass

        ty, tx = miny, minx

    print("Unit moved to x:{}, y:{}".format(tx, ty))
    return tx, ty

def solve_graph(graph, init, coord_list):
    ''' Recursive function to solve the graphs'''

    n_list = set()

    # Get all the neighboors of the coordinates in coord_list
    for x, y in init:

        # Del from coord list
        try: 
            del coord_list[coord_list.index((x, y))]
        except: 
            pass

    # Value for the neighboors
        val = graph[y, x] + 1

        # Evaluate and create neighboors
        for n_x, n_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (graph[n_y, n_x] > val):
                graph[n_y, n_x] = val

            if (n_x, n_y) in coord_list: 
                n_list.add((n_x, n_y))

    if n_list:
        graph, coord_list = solve_graph(graph,
                                        n_list,
                                        coord_list)
    return graph, coord_list

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
                units[n_unit] = Unit(x, y, char)
                n_unit += 1

    # Delete all units from the list
    for i in range(len(m)):
        m[i] = m[i].replace("G", ".")
        m[i] = m[i].replace("E", ".")

    return m, units
    
def get_walls(m):
    ''' Returns list of wall coordinates '''
    # Unit Dict
    walls = []
    # Create all units
    for y, line in enumerate(m):
        for x, char in enumerate(line):
            if char == "#":
                # Found a unit
                walls.append((x, y))

    return walls

order = lambda u: (u[1])
def order_units(units: dict) -> dict:
    ''' Orders the units by order '''

    sorted_list = sorted(
        [(k, (val.x, val.y)) for k, val in units.items()],
        key = order
    )
    return dict(zip([k for k in range(1, len(units)+1)],
                    [units[unit[0]] for unit in sorted_list])
    )

def print_units_position(units):
    ''' Just for debug '''
    print(sorted(
        [(k, (val.x, val.y), val.alive) for k, val in units.items()])
    )

def end_battle(units):
    ''' End battle if only enemies from one type exist '''

    if len(set([unit.t for unit in units.values()])) > 1:
        return 1
    else: 
        return 0

def run_battle(m, units, walls) -> None:
    ''' Runs part 1 '''

    while end_battle:
        units = order_units(units)

        for unit in units.values():
            if unit.alive:
                print("Unit on x:{}, y:{} moving.".format(
                    unit.x, unit.y))
                unit.turn(m, units, walls)
                print("")

# Solve Part 1
m, units = create_units(m)

# Get walls coordinates
walls = get_walls(m)

run_battle(m, units, walls)

