import re
input = open("day3input.txt", "r")
product = 0
for line in input:
    muls = re.findall(r'(mul\(\d{1,3}\,\d{1,3}\))', line)
    for mul in muls:
        nums = [int(x) for x in mul[4:-1].split(",")]
        product += nums[0] * nums[1]
print(product)