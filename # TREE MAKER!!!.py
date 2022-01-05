# TREE MAKER!!!
def tree(tree_base: int) -> str:
    print('A TREE HAS SPAWNED!')
    # create a box that represents the outline
    middle = tree_base - 1    # middle index is always tree_base - 1
    length = tree_base * 2 - 1
    height = tree_base + 1

    for i in range(0, height):
        stars = str('*'*length) # Start with a box of stars
        if i == height - 1: # this if statement makes the bottom lines always be the * in the middle
            left_whitespace = tree_base - 1 # for last line only
            right_whitespace = left_whitespace # for last line only
            stars = stars[:len(stars) - right_whitespace]
            stars = str(' '*left_whitespace + '*')
        elif i < height:
            left_whitespace = tree_base - (i + 1) # General formula
            right_whitespace = left_whitespace
            stars = stars[:len(stars) - right_whitespace] # Fix whitespace on left side
            stars = stars[:len(stars) - right_whitespace] # Once again, this time the right side
            stars = str(" "*left_whitespace + stars) # Correct spacing
        print(stars)



# You can test your function by calling it within the following block

if __name__ == "__main__":
    x = int(input('Enter a height for your tree: '))
    tree(x)
