def open_file(file):
    with open(file, 'r') as f:
        return [line.split() for line in f]

def day7_1():
    lines = open_file("Day 7/Day_7_input_test.txt")
    for i, line in enumerate(lines):
        if line[0] == '$':
            if line[1] == "cd":
                if line[2] == "/":
                     while line[0] 


                elif line[2] == "..":

                else: # It cn only be move in a directory

            else: # It caan only be ls

if __name__ == '__main__':
    print("The answer for day 7 part 1 is: ")
    day7_1()