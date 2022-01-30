data = []
with open("input8.txt") as file:
    for line in file:
        line = line.split("|")
        input = line[0].strip()
        input = input.split(" ")
        output = line[1].strip()
        output = output.split(" ")
        data.append([input, output])


output_values = 0
for line in data:
    code = {}
    for symbol in line[0]:
        if len(symbol) == 2:
            code[1] = symbol
        if len(symbol) == 4:
            code[4] = symbol
        if len(symbol) == 3:
            code[7] = symbol
        if len(symbol) == 7:
            code[8] = symbol
    for symbol in line[0]:
        if len(symbol) == 6:
            isNine = True
            isSixOrZero = False
            for character in code[4]:
                if character not in symbol:
                    isNine = False
                    isSixOrZero = True
            if isNine:
                code[9] = symbol
            if isSixOrZero:
                isZero = True
                for character in code[1]:
                    if character not in symbol:
                        isZero = False
                if isZero:
                    code[0] = symbol
                else:
                    code[6] = symbol
        if len(symbol) == 5:
            isThree = True
            isFiveOrTwo = False
            for character in code[1]:
                if character not in symbol:
                    isThree = False
                    isFiveOrTwo = True
            if isThree:
                code[3] = symbol
            if isFiveOrTwo:
                missing_bits = 0
                for character in code[4]:
                    if character not in symbol:
                        missing_bits += 1
                if missing_bits == 1:
                    code[5] = symbol
                else:
                    code[2] = symbol
    output2 = []
    for symbol in line[1]:
        for value, symbol2 in code.items():
            sorted_symbol_list = sorted(symbol)
            sorted_symbol_string = "".join(sorted_symbol_list)
            sorted_symbol_list2 = sorted(symbol2)
            sorted_symbol_string2 = "".join(sorted_symbol_list2)
            if sorted_symbol_string == sorted_symbol_string2:
                output2.append(value)
    strings = [str(integer) for integer in output2]
    a_string = "".join(strings)
    to_add = int(a_string)
    output_values += to_add


print(output_values)