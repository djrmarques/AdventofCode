from collections import deque


class game:

    def __init__ (self, n_players, l_marble_val):
        self.player_scores = dict(zip(range(1, int(n_players) + 1), [0] * int(n_players)))


    def run_game(self, n_players, l_marble_val):
        # Runs the game until last marble

        # Placeholder for the games marbles
        L = deque([0])
        n_marble = 1

        while 1:
            # Runs once for every player
            for player in range(1, n_players+1):

                if not self.is_m23(n_marble):
                    L.rotate(-1)
                    L.append(n_marble)

                else:
                    self.player_scores[player] += n_marble

                    L.rotate(7)
                    self.player_scores[player] += L.pop()
                    L.rotate(-1)

                if n_marble >= l_marble_val:
                    return self.player_scores
                else:
                    n_marble += 1

    def is_m23(self, n):
        if n % 23 == 0:
            return 1
        else:
            return 0 

def test_routine():
    ''' Runs routine and compares results with the test files '''
    file = '9/awked_test_list'
    with open(file, "r") as f:
        for line in f.readlines():
            n_players, l_marble_val, hscore = line.strip().split()
            g = game(n_players, l_marble_val)
            results = g.run_game(int(n_players), int(l_marble_val))
            print("{:<6} {}".format(max(results.values()),  int(hscore)))
            print(max(results.values()) ==  int(hscore))

# test_routine()

def solve_part1():
    file = '9/input'
    with open(file, "r") as f:
        n_players, l_marble_val = f.readline().strip().split()
        g = game(n_players, l_marble_val)
        results = g.run_game(int(n_players), int(l_marble_val))
        print(max(results.values()))

# 409832
# solve_part1()

def solve_part2():
    file = '9/input'
    with open(file, "r") as f:
        n_players, l_marble_val = f.readline().strip().split()
        g = game(n_players, l_marble_val)
        results = g.run_game(int(n_players), int(l_marble_val)*100)
        print(max(results.values()))

# solve_part2()
