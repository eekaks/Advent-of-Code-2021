def neighbours(point: tuple):
    points = []
    if point[0]+1 <= 9:
        points.append(point[0]+1, point[1])
    if point[0]-1 >= 0:
        points.append(point[0]-1, point[1])
    if point[1]+1 <= 9:
        points.append(point[0], point[1]+1)
    if point[1]-1 >= 0:
        points.append(point[0], point[1]-1)

    if point[0]+1 <= 9 and point[1]+1 <= 9:
        points.append(point[0]+1, point[1]+1)
    if point[0]+1 <= 9 and point[1]-1 >= 0:
        points.append(point[0]+1, point[1]-1)
    if point[0]-1 >= 0 and point[1]+1 <= 9:
        points.append(point[0]-1, point[1]+1)
    if point[0]-1 >= 0 and point[1]-1 >= 0:
        points.append(point[0]-1, point[1]-1)


grid = []
with open("input11.txt") as file:
    for line in file:
        line = line.strip()
        to_add = []
        for number in line:
            to_add.append(int(number))
        grid.append(to_add)


for i in range(100):
    new_grid = []
    for row in grid:
        add = []
        for number in row:
            add.append(number + 1)
            
