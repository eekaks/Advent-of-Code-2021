contents = []
with open("input6.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
        temp = line

school = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for number in temp:
        school[int(number)] += 1

print(school)

for a in range(256):
    new_school = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for timer, sum in school.items():
        if timer == 0:
            new_school[8] += sum
            new_school[6] += sum
        else:
            new_school[timer - 1] += sum
    school = new_school

summa = 0
for value in school.values():
    summa += value

print(summa)

