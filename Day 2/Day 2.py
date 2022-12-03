def open_file(file):
    with open(file, 'r') as f:
        return [line.split() for line in f]

def day2_1():
    '''
    A X -> Rock     -> 1 point
    B Y -> Paper    -> 2 points
    C Z -> Scissors -> 3 points
    '''
    points = 0
    lines = open_file("Day_2_input.txt")
    for line in lines:
        if line[0] == 'A':
            if line[1] == 'X':
                points += 4 # Draw
            elif line[1] == 'Y':
                points += 8 # Win
            else:
                points += 3 # Lose
        elif line[0] == 'B':
            if line[1] == 'X':
                points += 1 # Lose
            elif line[1] == 'Y':
                points += 5 # Draw
            else:
                points += 9 # Win
        else:
            if line[1] == 'X':
                points += 7 # Win
            elif line[1] == 'Y':
                points += 2 # Lose
            else:
                points += 6 # Draw
        
    print(points)
    
def day2_2():
    '''
    A -> Rock       -> 1 point
    B -> Paper      -> 2 points
    C -> Scissors   -> 3 points
    X -> Lose       -> 0 points
    Y -> Draw       -> 3 points
    Z -> Win        -> 6 points
    '''
    points = 0
    lines = open_file("Day_2_input.txt")
    for line in lines:
        if line[0] == 'A':
            if line[1] == 'X':
                points += 3 # Lose with C
            elif line[1] == 'Y':
                points += 4 # Draw with A
            else:
                points += 8 # Win with B
        elif line[0] == 'B':
            if line[1] == 'X':
                points += 1 # Lose with A
            elif line[1] == 'Y':
                points += 5 # Draw with B
            else:
                points += 9 # Win with C
        else:
            if line[1] == 'X':
                points += 2 # Lose with B
            elif line[1] == 'Y':
                points += 6 # Draw with C
            else:
                points += 7 # Win with A
        
    print(points)

if __name__ == '__main__':
    print("The answer for day 1 part 1 is: ")
    day2_1()

    print("\nThe answer for day 1 part 2 is: ")
    day2_2()