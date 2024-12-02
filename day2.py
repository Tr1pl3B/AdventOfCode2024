def isSafe(numbers):
    for i in range(len(numbers)-1):
        if increasing and numbers[i+1] <= numbers[i] or 3 < numbers[i+1] - numbers[i]:
            return False

        elif not increasing and numbers[i] <= numbers[i+1] or 3 < numbers[i] - numbers[i+1]:
            return False
    return True

reprots = open("day2input.txt", "r")
safeReports = 0
for line in reprots:
    numbers = line.split(" ")
    numbers = [int(x) for x in numbers]
    safeReport = True
    increasing = True if numbers[0] < numbers[len(numbers)-1] else False
    if isSafe(numbers):
        safeReports += 1
    else:
        for i in range(len(numbers)):
            cutNubers = numbers.copy()
            cutNubers.pop(i)
            if isSafe(cutNubers):
                safeReports += 1
                break
print(safeReports)