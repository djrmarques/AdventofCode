class Cart:

    def __init__(self, x, y, direction):
        self.inter = 'l'
        self.x = x
        self.y = y
        self.drct = direction

    def move(self, track):
        ''' Moves one step '''
        pass

    def turn(self, tile):
        ''' Turn cart '''
        if self.drct == '>' and tile == '/':
            return '^'
        if self.drct == '>' and tile == '\\':
            return 'v'
        if self.drct == 'v' and tile == '/':
            return '<'
        if self.drct == 'v' and tile == '\\':
            return '>'
        if self.drct == '^' and tile == '/':
            return '>'
        if self.drct == '^' and tile == "\\" :
            return '<'
        if self.drct == '<' and tile == '/':
            return 'v'
        if self.drct == '<' and tile == '\\':
            return '^'


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

    # Order of the dicts based on the  
    pos_list = sorted([(k, (a.x, a.y)) for k, a in carts.items()], key=order)
    return dict(zip(sorted(carts), [carts[k[0]] for k in pos_list]))

def verify_crash(carts):
    ''' Runs through all the carts to verify if there is a crash '''
    pass

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

    # Move carts one by one
    for key, cart in carts.items():
        cart.move(track)


file = '13/input'
file = '13/test-input'
with open(file, 'r')  as f:
    lines = f.readlines()

# Get carts pos
cart_signs = ['v', '>', '<', '^']

# Create Carts
carts = create_carts(lines, cart_signs)

# Split track into list
# This will make it easier to compare
track = prepare_track(lines, cart_signs)


