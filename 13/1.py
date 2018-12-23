class Cart:

    def __init__(self, x, y, direction):
        self.inter = 'l'
        self.x = x
        self.y = y
        self.drct = direction
        self.alive = 1

    def move(self, track):
        ''' Moves one step '''

        # Gets nest position
        x, y = self.next_position()

        # Get next tile on track
        try:
            tile = track[y][x]
        except: raise Exception("Cart Pos:\n x:{} y:{} direction:{}\nNext Position: x:{} y:{}".format(self.x, self.y, self.drct, x, y))

        if tile in ['/', '\\']:
            self.turn(tile)
        elif tile == '+':
            self.cross()
        self.x, self.y = x, y

    def next_position(self):
        ''' Returns the coordinates for the nest position '''
        if self.drct == '>':
            return self.x + 1, self.y
        if self.drct == '<':
            return self.x - 1, self.y
        if self.drct == 'v':
            return self.x , self.y+1
        if self.drct == '^':
            return self.x, self.y-1
        else:
            raise Exception("Unknow Symbol: ".format(self.drct))

    def turn(self, tile):
        ''' Turn cart '''
        if self.drct == '>' and tile == '/':
            self.drct = '^'
        elif self.drct == '>' and tile == '\\':
            self.drct = 'v'
        elif self.drct == 'v' and tile == '/':
            self.drct = '<'
        elif self.drct == 'v' and tile == '\\':
            self.drct = '>'
        elif self.drct == '^' and tile == '/':
            self.drct = '>'
        elif self.drct == '^' and tile == "\\" :
            self.drct = '<'
        elif self.drct == '<' and tile == '/':
            self.drct = 'v'
        elif self.drct == '<' and tile == '\\':
            self.drct = '^'

    def cross(self):
        ''' Defines the turn at a cross '''
        if self.inter == 'l':
            if self.drct == '>':
                self.drct = '^' 
            elif self.drct == '<':
                self.drct = 'v' 
            elif self.drct == 'v':
                self.drct = '>' 
            elif self.drct == '^':
                self.drct = '<' 
            self.inter = 's'

        elif self.inter == 's':
            self.inter = 'r'
            
        elif self.inter == 'r':
            if self.drct == '>':
                self.drct = 'v' 
            elif self.drct == '<':
                self.drct = '^' 
            elif self.drct == 'v':
                self.drct = '<' 
            elif self.drct == '^':
                self.drct = '>' 
            self.inter = 'l'
def create_carts(lines: list, cart_signs: list) -> dict:
    ''' Creats all the carts and returns a dict '''

    cart_dicts = {}
    n_cart = 1

    for y, line in enumerate(lines):
        for x, char in enumerate(line.rstrip()):
            if char in cart_signs:
                cart_dicts[n_cart] = Cart(x, y, char)
                n_cart += 1

    return cart_dicts


order = lambda x: x[1]
def order_carts(carts: dict) -> dict:
    ''' Returns the ordered dict ''' 
    # Remove dead carts
    dead_carts = []
    for k, val in carts.items():
        if not val.alive:
            dead_carts.append(k)

    for dead_cart in dead_carts:
        del carts[dead_cart]

    # Order of the dicts based on the  
    pos_list = sorted([(k, (a.x, a.y)) for k, a in carts.items()], key=order)
    return dict(zip(sorted(carts), [carts[k[0]] for k in pos_list]))

def verify_crash(carts):
    ''' Runs through all the carts to verify if there is a crash '''
    crashes = 0
    coords = {}
    crashed_carts = []
    for k1, val1 in carts.items():
        for k2, val2 in carts.items():
                if(((val1.x, val1.y) == (val2.x, val2.y)) and k1 != k2):
                    crashed_carts.append(((k1, k2), val1))
                    val1.alive = 0
                    val2.alive = 0
                    crashes =  1

    # for crashed in sorted(crashed_carts):
    #     print("Carts: {} in x:{}, y:{}".format(crashed[0], crashed[1].x, crashed[1].y))
    
    return crashes

def prepare_track(lines: list, cart_signs: list) -> list:
    ''' Splits strings into lists and replace the cart '''

    repl = dict(zip(cart_signs, ('|', '-', '-', '|')))
    track = []
    for line in lines:
        line_list = [a if a not in cart_signs else repl[a] for a in line.rstrip()]
        track.append(line_list)
    return track

def step(carts: dict, track: list) -> dict:
    ''' Advances one step '''

    # Orders Carts
    carts = order_carts(carts)
    print(len(carts))

    # Only one cart left
    if len(carts) == 1: 
        return 0 

    # Move carts one by one
    for key, cart in carts.items():
        cart.move(track)


def show_coordinates(carts):
    ''' Prints the coordinates of all the carts for DEBUBG ''' 
    for k, val in carts.items():
        print('Cart {} in x:{} and y:{} and Direction: {}'.format(k, val.x, val.y, val.drct))

    print('')

file = '13/input'
# file = '13/test-input'
with open(file, 'r')  as f:
    lines = f.readlines()

# Get carts pos
cart_signs = ['v', '>', '<', '^']

# Create Carts
carts = create_carts(lines, cart_signs)

# Split track into list
# This will make it easier to compare
track = prepare_track(lines, cart_signs)

while (len(carts)>1):
    step(carts, track)
    verify_crash(carts)

print(list(carts.values())[0].x, list(carts.values())[0].y)
