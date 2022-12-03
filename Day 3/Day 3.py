def open_file(file):
    with open(file, 'r') as f:
        return [line.split() for line in f]

def day3_1():
    first_half = []
    second_half = []
    priority = 0
    lines = open_file("Day_3_input.txt")
    for line in lines:
        for i, letter in enumerate(line[0]):
            if i < len(line[0])/2:
                first_half.append(letter)
            else:
                second_half.append(letter)
        
        set_1 = set(first_half)
        set_2 = set(second_half)

        for letter in set_1:
            if letter in set_2:
                #print(letter)
                if letter.islower():
                    priority += ord(letter) - ord('a') + 1
                else:
                    priority += ord(letter) - ord('A') + 27  
            
        first_half = []
        second_half = []

    print(priority)

def day3_2():
    priority = 0
    lines = open_file("Day_3_input.txt")

    for i in range(0, len(lines), 3):
        #print(lines[i:i+3])
        primera = set(lines[i][0])
        segunda = set(lines[i+1][0])
        tercera = set(lines[i+2][0])

        for letter in primera:
            if letter in segunda and letter in tercera:
                #print(letter)
                if letter.islower():
                    priority += ord(letter) - ord('a') + 1
                else:
                    priority += ord(letter) - ord('A') + 27 

    print(priority)
    

if __name__ == '__main__':
    print("The answer for day 3 part 1 is: ")
    day3_1()

    print("\nThe answer for day 3 part 2 is: ")
    day3_2()