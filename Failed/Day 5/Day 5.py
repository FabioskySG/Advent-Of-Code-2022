def open_file(file):
    with open(file, 'r') as f:
        return [line.split(" ") for line in f]

def day5_1():
    '''
    move X from Y to Z:
    X -> cuantas cajas muevo
    Y -> columna origen
    Z -> columna destino
    '''
    origin = []
    destination = []
    moved = []
    lines = open_file("Day 5/Day_5_input_test.txt")
    
    for row, line in enumerate(lines):
        #print(line)

        if line[-1] == "\n":
            line.pop() # Elimino los \n

        if len(line) != 0:
            if line[0] == "move":
                moved += line[1]
                origin += line[3]
                destination += line[5] # Works until this point

            elif line[1] == "1":
                #columns = int(line[-1]) # Obtain number of columns
                rows = row
    '''
    letter_list = []
    positions = []
    for row, line in enumerate(lines):
        if row < rows:
            for col, letter in enumerate(line):
                if letter.isupper():
                    positions += [(row, col)]
                    letter_list += [letter[1]]


    print(moved)
    print(positions)
    print(letter_list)
    '''
    fils = []
    columns = 0
    # ME RINDO

if __name__ == '__main__':
    print("The answer for day 5 part 1 is: ")
    day5_1()

    #print("\nThe answer for day 5 part 2 is: ")
    #day5_2()