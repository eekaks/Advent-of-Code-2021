crabs = []
with open("input7.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
        for crab in line:
            crabs.append(int(crab))

crabs = sorted(crabs)
median = crabs[len(crabs)//2]
print(median)

fuel_consumption = 0
for crab in crabs:
    fuel_consumption += abs(crab-median)

print(fuel_consumption)




sum = 0
for crab in crabs:
    sum += crab

average = sum/len(crabs)

print(average)

def consumption(start):
    if start > 466:
        sum1 = 0
        add = 1
        while start > 466:
            start -= 1
            sum1 += add
            add += 1
        return sum1
    elif start < 466:
        sum2 = 0
        add = 1
        while start < 466:
            start += 1
            sum2 += add
            add += 1
        return sum2
    else:
        return 0

fuel_consumption = 0
for crab in crabs:
    fuel_consumption += consumption(crab)

print(fuel_consumption)