def open_file(file):
    with open(file, 'r') as f:
        return [line.split() for line in f]

def day1_1():
    calories = 0
    max = 0
    lines = open_file("Day_1_input.txt")
    for line in lines:
        if len(line) != 0:
            calories = calories + int(line[0])
        else:
            calories = 0
        
        if calories > max:
            max = calories
    print(max)

def day1_2():
    calories = 0
    cal_elves = []
    top3 = 0
    lines = open_file("Day_1_input.txt")
    for line in lines:
        if len(line) != 0:
            calories += int(line[0])
        else:
            cal_elves.append(calories)
            calories = 0
    
    for _ in range(3):
        top3 += cal_elves.pop(cal_elves.index(max(cal_elves)))

    print(top3)

if __name__ == '__main__':
    print("The answer for day 1 part 1 is: ")
    day1_1()

    print("\nThe answer for day 1 part 2 is: ")
    day1_2()
