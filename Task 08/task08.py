import math

def game_tree(depth, pos, max_player, leafs, height):
    if depth == height:
        return leafs[pos]
    
    left_child = pos * 2
    right_child = pos * 2 + 1
    
    if max_player:
        v1 = game_tree(depth+1, left_child, False, leafs, height)
        v2 = game_tree(depth+1, right_child, False, leafs, height)
        best = max(v1, v2)
        side = "left" if v1 >= v2 else "right"
        print(f"Level {depth} (MAX): {v1} and {v2} -> pick {best} ({side})")
        return best
    else:
        v1 = game_tree(depth+1, left_child, True, leafs, height)
        v2 = game_tree(depth+1, right_child, True, leafs, height)
        best = min(v1, v2)
        side = "left" if v1 <= v2 else "right"
        print(f"Level {depth} (MIN): {v1} and {v2} -> pick {best} ({side})")
        return best

print("Welcome Minimax Program")
n = int(input("How many leaf node you want (only power of 2): "))

if (n & (n-1)) != 0 or n <= 0:
    print("Wrong input! must be 4,8,16,32 only")
    exit()

leafs = []
for i in range(n):
    x = int(input(f"Enter value {i+1}: "))
    leafs.append(x)

height = int(math.log2(n))

who = input("Who play first max or min: ").lower()
start_max = (who == "max")

print("Your leaf values:", leafs)
print("Total depth is:", height)
print("First player is:", "MAX" if start_max else "MIN")
print("")
print("Start calculating...")

result = game_tree(0, 0, start_max, leafs, height)

print("")
print("Finish!")
print("Best value at root:", result)
if start_max:
    print("MAX player will win with this value")
else:
    print("MIN player will force this value")