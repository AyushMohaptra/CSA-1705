import itertools
import re

def solve_cryptarithmetic(puzzle):
    """Solves a cryptarithmetic puzzle using a compact brute-force approach."""
    p_upper = puzzle.upper()
    words = re.findall('[A-Z]+', p_upper)
    letters = "".join(sorted(set("".join(words))))

    if len(letters) > 10:
        print(f"'{puzzle}': Invalid, more than 10 unique letters.")
        return

    first_letters = {word[0] for word in words}
    
    for p in itertools.permutations('0123456789', len(letters)):
        table = str.maketrans(letters, "".join(p))

        # CONSTRAINT: Check for leading zeros in any word.
        if '0' in {char.translate(table) for char in first_letters}:
            continue

        try:
            # Translate the puzzle into a numeric equation and evaluate it.
            equation = p_upper.replace('=', '==').translate(table)
            if eval(equation):
                print(f"Solution: {puzzle} -> {equation.replace('==', '=')}")
                return
        except (SyntaxError, ValueError):
            # Continue if the translated string is not a valid equation.
            continue
            
    print(f"Solution: {puzzle} -> No solution found.")

# --- Main execution block ---
if __name__ == "__main__":
    puzzles = ["SEND + MORE = MONEY", "TWO + TWO = FOUR", "CROSS + ROADS = DANGER"]
    for p in puzzles:
        solve_cryptarithmetic(p)