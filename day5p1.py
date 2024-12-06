rules = [x.removesuffix("\n").split("|") for x in open("day5input.txt").readlines() if x.__contains__("|")]
printOrder = [x.removesuffix("\n").split(",") for x in open("day5input.txt").readlines() if x.__contains__(",")]
rules = [[int(x) for x in y] for y in rules]
printOrder = [[int(x) for x in y] for y in printOrder]

middlePageNumbers = 0
valid = True
for order in printOrder:
    for rule in rules:
        try:
            if order.index(rule[1]) < order.index(rule[0]):
                valid = False
                break
        except:
            pass
    if valid:
        middlePageNumbers += order[(int)(len(order) / 2 )]
    valid = True
print(middlePageNumbers)
