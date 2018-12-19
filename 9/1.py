
class game:

    def __init__ (self, n_players, l_marble_val):
        self.player_scores = dict(zip(range(1, int(n_players) + 1), [0] * int(n_players)))


    def run_game(self, n_players, l_marble_val):
        # Runs the game until last marble

        # Placeholder for the games marbles
        L = [0]
        n_marble = 1
        current_marble_pos = 0

        while 1:
            # Runs once for every player
            for player in range(1, n_players+1):

                if not self.is_m23(n_marble):
                    if (current_marble_pos + 2) <= len(L):
                        current_marble_pos += 2
                    else:
                        current_marble_pos = current_marble_pos + 2 - len(L)
                    L.insert(current_marble_pos, n_marble)
                else:
                    self.player_scores[player] += n_marble

                    # Remove the 7th counter clockwise marble
                    if current_marble_pos - 7 < 0:
                        remove_marble = current_marble_pos - 7 + len(L)
                    else:
                        remove_marble = current_marble_pos - 7

                    self.player_scores[player] += L[remove_marble]
                    del L[remove_marble]

                    current_marble_pos = remove_marble 

                # print("{}: {}".format(player, L))
                if n_marble >= l_marble_val:
                    return self.player_scores
                else:
                    # Increments marble number
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
            # print("{:<6} {}".format(max(results.values()),  int(hscore)))
            print(max(results.values()) ==  int(hscore))

def solve():
    file = '9/input'
    with open(file, "r") as f:
        n_players, l_marble_val = f.readline().strip().split()
        g = game(n_players, l_marble_val)
        results = g.run_game(int(n_players), int(l_marble_val))
        print(max(results.values()))

solve()


