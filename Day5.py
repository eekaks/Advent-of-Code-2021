class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

vents = []
with open("input5.txt") as file:
    for line in file:
        line = line.strip()
        start_end = line.split(" ")
        start = start_end[0].split(",")
        x1 = start[0]
        y1 = start[1]
        end = start_end[2].split(",")
        x2 = end[0]
        y2 = end[1]
        vents.append(Vent(int(x1), int(y1), int(x2), int(y2)))



coordinates = {}
for vent in vents:
    if vent.y1 == vent.y2:
        if vent.x1 < vent.x2:
            for x in range(vent.x1, vent.x2+1):
                if (x, vent.y1) not in coordinates:
                    coordinates[(x, vent.y1)] = 1
                else:
                    coordinates[(x, vent.y1)] += 1
        if vent.x1 > vent.x2:
            for x in range(vent.x2, vent.x1+1):
                if (x, vent.y1) not in coordinates:
                    coordinates[(x, vent.y1)] = 1
                else:
                    coordinates[(x, vent.y1)] += 1
    elif vent.x1 == vent.x2:
        if vent.y1 < vent.y2:
            for y in range(vent.y1, vent.y2+1):
                if (vent.x1, y) not in coordinates:
                    coordinates[(vent.x1, y)] = 1
                else:
                    coordinates[(vent.x1, y)] += 1
        if vent.y1 > vent.y2:
            for y in range(vent.y2, vent.y1+1):
                if (vent.x1, y) not in coordinates:
                    coordinates[(vent.x1, y)] = 1
                else:
                    coordinates[(vent.x1, y)] += 1
    else:
        y = vent.y1
        if vent.x1 > vent.x2:
            for x in range(vent.x1, vent.x2-1, -1):
                if (x, y) not in coordinates:
                    coordinates[(x, y)] = 1
                else:
                    coordinates[(x, y)] += 1
                if vent.y1 > vent.y2:
                    y -= 1
                elif vent.y1 < vent.y2:
                    y += 1
        if vent.x1 < vent.x2:
            for x in range(vent.x1, vent.x2+1):
                if (x, y) not in coordinates:
                    coordinates[(x, y)] = 1
                else:
                    coordinates[(x, y)] += 1
                if vent.y1 > vent.y2:
                    y -= 1
                elif vent.y1 < vent.y2:
                    y += 1

sum = 0
for coordinate, value in coordinates.items():
    if value > 1:
        sum += 1

print(sum)

