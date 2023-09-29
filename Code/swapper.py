# Take a text input (rubik's cube notation) and reverse it

# L' U2 L U L' U L would be
# L' U' L U' L' U2 L

def swapper(notation):
    notation = notation.split()
    new_notation = []
    for i in range(len(notation)):
        match notation[i]:
            case "U" : "U'"
            case "U'" : "U"
            case "D" : "D'"
            case "D'" : "D"
            case "L" : "L'"
            case "L'" : "L"
            case "R" : "R'"
            case "R'" : "R"
            case "F" : "F'"
            case "F'" : "F"
            case "B" : "B'"
            case "B'" : "B"
            case _ : i
        new_notation.append(i)
    new_notation.reverse()
    print(new_notation)

swapper("L' U2 L U L' U L")