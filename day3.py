import re
input = open("day3input.txt", "r")
product = 0
do = True
for line in input:
    # Find all instances of mul(x,y) and calculate the product of x and y
    # muls = re.findall(r'(mul\(\d{1,3}\,\d{1,3}\))', line)
    
    # Find all instances of mul(x,y), do() and don't() and calculate the product of x and y according to the do() and don't() functions
    mulsDoDotn = re.findall(r'(mul\(\d{1,3}\,\d{1,3}\))|(do\(\))|(don\'t\(\))', line)
    for tuple in mulsDoDotn:
        if tuple[0] and do:
            nums = [int(x) for x in tuple[0][4:-1].split(",")]
            product += nums[0] * nums[1]
        elif tuple[1]:
            do = True
        elif tuple[2]: 
            do = False
print(product)