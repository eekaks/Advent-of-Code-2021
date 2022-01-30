dict = {")":"(", "]":"[", "}":"{", ">":"<"}
scores = {")":3, "]":57, "}":1197, ">":25137}
score = 0

incompletes = []

with open("input10.txt") as file:
    for line in file:
        line = line.strip()
        to_add = True
        seen_chars = []
        for character in line:
            if character in dict:
                opposite_piece = seen_chars.pop()
                if opposite_piece != dict[character]:                
                    score += scores[character]
                    to_add = False
                    break
            else:
                seen_chars.append(character)
        if to_add:
            incompletes.append(line)


values = {"(":1, "[":2, "{":3, "<":4}
line_scores = []
for line in incompletes:
    seen = []
    for character in line:
        if character in dict:
            x = seen.pop()        
        else:
            seen.append(character)
    line_score = 0
    while seen:
        line_score = line_score * 5 + values[seen.pop()]
    line_scores.append(line_score)

sorted_scores = sorted(line_scores)

print(sorted_scores)

print(sorted_scores[len(sorted_scores)//2])