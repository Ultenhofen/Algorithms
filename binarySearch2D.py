# Binary search algorithm for 2D matrices
# Because Python likes to excercise it's power over me
# whenever a value is chosen that has coordinates {C,C}
# where C is any number, Python will simplify the array down to just {0}
# instead of {0,0}

def BS(k, list, x, y):
    print(x , y)
    if (len(list)-1 < y): # Checks if value is actually in matrix
        return "Not Found"
    if (list[y][x] == k): # Checks if value has been found
        c = {y , x}
        return c
    if (x == -1): # Extra base case just in case
        return "Not Found Loser"
    if (list[y][x] < k): # Checks if k is in row
        y += 1
        return BS(k, list, x, y)
    if (list[y][x] > k): # Checks if k is greater than the indexed value
        x -= 1
        return BS(k, list, x, y)

def binarySearch(k , list):
    x = len(list[0])-1
    y = 0
    if (list[y][x] == k): # Checks if value is in the starting spot
        c = {y , x}
        return c
    elif (list[y][x] > k): # Checks if k is greater than the indexed value
        x -= 1
        return BS(k, list, x, y)
    elif (list[y][x] < k): # Checks if k is in row
        y += 1
        return BS(k, list, x, y)
    else: # Not in matrix
        return "Not Found"

# Main
list = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10,11,12]]

print(binarySearch(1, list))
