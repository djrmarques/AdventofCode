class elf:
    ''' Elf Class '''
    def __init__(self, recipe, ind):
        self.current_recipe = recipe
        self.current_index = ind

    def pick_recipe(self, recipe_list):
        new_index = 1 + int(self.current_recipe) + self.current_index

        while new_index >= len(recipe_list):
            new_index -= len(recipe_list)
        self.current_index = new_index

        self.current_recipe = recipe_list[self.current_index]


# Input List
input = "554401"
# input = "59414
# input = "92510"

size_input = len(input)

recipe_list = "37"
elf1 = elf("3", 0)
elf2 = elf("7", 1)

def solve1(input, recipe_list):
    for _ in range(int(input) + 10):

        sum_recipes = str(int(elf1.current_recipe) + int(elf2.current_recipe))

        # Separate recipes and append the new recipes to the list
        recipe_list += str(sum_recipes)

        # Elfes pick new recipes
        elf1.pick_recipe(recipe_list)
        elf2.pick_recipe(recipe_list)


    print("Part 1: ", recipe_list[int(input):int(input)+10])

def solve2(recipe_list, input):
    while input not in recipe_list[-7:]:
        sum_recipes = str(int(elf1.current_recipe) + int(elf2.current_recipe))

        # Separate recipes and append the new recipes to the list
        recipe_list += str(sum_recipes)

        # Elves pick new recipes
        elf1.pick_recipe(recipe_list)
        elf2.pick_recipe(recipe_list)

    if input ==  recipe_list[-6:]:
        print("Part2: ", len(recipe_list) -size_input)
    else: 
        print("Part2: ", len(recipe_list) - (size_input + 1))

solve1(input, recipe_list)

# Restart
recipe_list = "37"
elf1 = elf("3", 0)
elf2 = elf("7", 1)
solve2(recipe_list, input)
