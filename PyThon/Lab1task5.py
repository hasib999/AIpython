plus = "+"
hypen = "-"
HLine = "|"
counthp = 0

for x in range(3):
    countline = x
    for p in range(3):
        print(plus, end="")
        counthp = p
        for hp in range(4):
            if counthp == 2:
                break
            else:
                print(hypen, end="")
    print("")
    for y in range(4):
        if countline == 2:
            break
        else:
            print(HLine, "  ", HLine, "  ", HLine)



