# þetta er einfaldur tölvuleikur þar sem notandinn á að fara frá púnt A til púnt B
block_1 = 1
block_2 = 1
def is_valid_dir(diregson):
    if block_1 == 1 and block_2 == 1:
        if diregson == "n":
            return True
        else: 
            return False
    if block_1 == 1 and block_2 == 2:
        if diregson == "n" or diregson == "s" or diregson == "e":
            return True
        else: 
            return False
    if block_1 == 1 and block_2 == 3:
        if diregson == "s" or diregson == "e":
            return True
        else:
            return False
    if block_1 == 2 and block_2 == 1:
        if diregson == "n":
            return True
        else:
            return False
    if block_1 == 2 and block_2 == 2:
        if diregson == "s" or diregson == "w":
            return True
        else:
            return False
    if block_1 == 2 and block_2 == 3:
        if diregson == "e" or diregson == "w":
            return True
        else:
            return False
    if block_1 == 3 and block_2 == 1:
        if diregson == "n":
            return True
        else:
            return False
    if block_1 == 3 and block_2 == 2:
        if diregson == "s" or diregson == "n":
            return True
        else:
            return False
    if block_1 == 3 and block_2 == 3:
        if diregson == "n" or diregson == "s" or diregson == "w":
            return True
        else:
            return False

def directions(block_1, block_2):
    if block_1 == 1 and block_2 == 1:
        valid_dir = "(N)orth." 
    if block_1 == 1 and block_2 == 2:
        valid_dir = "(N)orth or (E)ast or (S)outh."
    if block_1 == 1 and block_2 == 3:
        valid_dir = "(E)ast or (S)outh."
    if block_1 == 2 and block_2 == 1:
        valid_dir = "(N)orth."
    if block_1 == 2 and block_2 == 2:
        valid_dir = "(S)outh or (W)est."
    if block_1 == 2 and block_2 == 3:
        valid_dir = "(E)ast or (W)est."
    if block_1 == 3 and block_2 == 1:
        valid_dir = "(N)orth."
    if block_1 == 3 and block_2 == 2:
        valid_dir = "(N)orth or (S)outh."
    if block_1 == 3 and block_2 == 3:
        valid_dir = "(N)orth or (S)outh or (W)est."
    return valid_dir
    
while True:
    directions_1 = directions(block_1, block_2)
    print("You can travel:", directions_1)
    diregson = input("Direction: ")
    diregson = diregson.lower()

    if is_valid_dir(diregson) == False:
        print("Not a valid direction!")
        continue

    if diregson == "q":
        break

    if block_1 >= 1 and block_1 <= 3 and block_2 >= 1 and block_2 <= 3:
        if diregson == "n": 
            block_2 += 1

        if diregson == "s":
            block_2 -= 1
    
        if diregson == "e":
            block_1 += 1

        if diregson == "w":
            block_1 -= 1
    
    if block_1 == 3 and block_2 == 1:
        print("Victory!")
        break

   