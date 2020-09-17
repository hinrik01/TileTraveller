# þetta er einfaldur tölvuleikur þar sem notandinn á að fara frá púnt A til púnt B
block_1 = 1
block_2 = 1

while True:
    you_can_travel = print()
    diragson = input("Direction: ")
    
    if diragson == "q":
        break

    if block_1 >= 1 and block_1 <= 3 and block_2 >= 1 and block_2 <= 3:
        if diragson == "n": 
            block_2 += 1

        if diragson == "s":
            block_2 -= 1
    
        if diragson == "e":
            block_1 += 1

        if diragson == "w":
            block_1 -= 1
    print(block_1, block_2)