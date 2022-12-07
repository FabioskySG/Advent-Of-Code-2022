def open_file(file):
    with open(file, 'r') as f:
        return [line for line in f]

def day6_1():
    lines = open_file("Day 6/Day_6_input_test.txt")
    for i, letter in enumerate(lines[0]):
        if i == 0 or i == 1 or i == 2:
            pass

        else:
            if letter != lines[0][i-3] and letter != lines[0][i-2] and letter != lines[0][i-1]:
                if lines[0][i-3] != lines[0][i-2] and lines[0][i-3] != lines[0][i-1]:
                    if lines[0][i-2] != lines[0][i-1]:
                        print(i+1)
                        break

def day6_2():
    list_14 = []
    lines = open_file("Day 6/Day_6_input.txt")
    for i, letter in enumerate(lines[0]):
        if i < 14:
            list_14 += [letter]

        else:
            if len(set(list_14)) == 14:
                print(i)
                break
            
            else:
                list_14.pop(0)
                list_14 += [letter]

if __name__ == '__main__':
    print("The answer for day 6 part 1 is: ")
    day6_1()

    print("The answer for day 6 part 2 is: ")
    day6_2()