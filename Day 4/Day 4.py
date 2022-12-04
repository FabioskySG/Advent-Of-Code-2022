def open_file(file):
    with open(file, 'r') as f:
        return [line.split() for line in f]

def day4_1():
    overlaps = 0
    lines = open_file("Day_4_input.txt")
    for line in lines:
        splitted = line[0].split(",")
        first_elf = splitted[0].split("-")
        second_elf = splitted[1].split("-")

        if (int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])) or (int(second_elf[0]) <= int(first_elf[0]) and int(second_elf[1]) >= int(first_elf[1])):
            overlaps += 1

    print(overlaps)

def day4_2():
    overlaps = 0
    lines = open_file("Day_4_input.txt")
    for line in lines:
        splitted = line[0].split(",")
        first_elf = splitted[0].split("-")
        second_elf = splitted[1].split("-")

        if (int(first_elf[1]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1])) or (int(second_elf[0]) >= int(first_elf[0]) and int(second_elf[0]) <= int(first_elf[1])):
            overlaps += 1
        
        elif (int(first_elf[1]) >= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1]) and int(first_elf[0]) <= int(second_elf[1])) or (int(second_elf[0]) <= int(first_elf[0]) and int(second_elf[0]) <= int(first_elf[1]) and int(second_elf[1]) >= int(first_elf[0])):
            overlaps += 1

        # Checkeo valores iguales
        elif ((int(first_elf[0]) == int(second_elf[1])) or (int(first_elf[1]) == int(second_elf[0])) or (int(first_elf[0]) == int(second_elf[1])) or (int(first_elf[1]) == int(second_elf[1]))):
            overlaps += 1

    print(overlaps)

if __name__ == '__main__':
    print("The answer for day 4 part 1 is: ")
    day4_1()

    print("\nThe answer for day 4 part 2 is: ")
    day4_2()