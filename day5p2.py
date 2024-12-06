def checkValidity(order):
    for rule in rules:
        try:
            if order.index(rule[1]) < order.index(rule[0]):
                return False
        except:
            pass
    return True

def undoError(order):
    for rule in rules:
        try:
            if order.index(rule[1]) < order.index(rule[0]):
                order[order.index(rule[0])], order[order.index(rule[1])] = order[order.index(rule[1])], order[order.index(rule[0])]
                return order
        except:
            pass
    return order


rules = [x.removesuffix("\n").split("|") for x in open("day5input.txt").readlines() if x.__contains__("|")]
printOrder = [x.removesuffix("\n").split(",") for x in open("day5input.txt").readlines() if x.__contains__(",")]
rules = [[int(x) for x in y] for y in rules]
printOrder = [[int(x) for x in y] for y in printOrder]

middlePageNumbers = 0
valid = True
for order in printOrder:
    if not checkValidity(order):
        while not checkValidity(order):
            order = undoError(order)
        middlePageNumbers += order[(int)(len(order) / 2 )]
    valid = True
print(middlePageNumbers)
