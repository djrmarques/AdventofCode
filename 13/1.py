class cart:

    def __init__(self, x, y, direction):
        self.turn = 'l'
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        pass

file = '13/input'
file = '13/test-input'
with open(file, 'r')  as f:
    lines = f.readlines()

# Get carts pos
cart_signs = ['v', '>', '<', '^']
