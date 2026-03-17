from itertools import permutations
people = ["John", "Silva", "Nichole", "Daniel"]
clues = [
    "John is younger than Silva",
    "Nichole is the youngest",
    "Daniel is the oldest"
]
print("=== LOGIC PUZZLE ===")
print(f"People to arrange: {people}")
print(f"\nClues:")
for i, clue in enumerate(clues, 1):
    print(f"  {i}. {clue}")

print("\n=== CHECKING ALL ARRANGEMENTS ===")

for arrangement in permutations(people):
    John = arrangement.index("John")
    Silva = arrangement.index("Silva")
    Nichole = arrangement.index("Nichole")
    Daniel = arrangement.index("Daniel")

    # Check all 3 clues
    clue1 = Silva < John          # A is before B
    clue2 = Nichole == 3         # C is not first
    clue3 = Daniel == 0       # D is last

    if clue1 and clue2 and clue3:
        print(f"✓ Valid solution: {arrangement}")
    else:
        print(f"✗ Invalid:        {arrangement}")

