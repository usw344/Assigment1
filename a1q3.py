##Muhammad Usman Ahmed
##mua942
##11275853
##Assigment 1 Question 3


def getSquare(textfile):
    '''
    reads any text file that follows the Torus format
    :param textfile: a text file containing the torus information
    :return: a 3x3 list of lists
    '''
    raw = open(textfile, "r")
    square = []
    lines = raw.readlines()

    ## delete everything that isn't the square section
    del lines[3:]
    for line in lines:
        subList = []
        line = line.rstrip()
        line = line.split(" ")
        subList = [int(x) for x in line]
        square.append(subList)
    return square


def getCommands(textfile):
    '''
    reads any text file that follows the Torus format
    :param textfile: a text file containing the torus information
    :return: a list of lists containing a command letter and an indice.
    '''
    raw = open(textfile, "r")
    commands = []
    lines = raw.readlines()
    ## delete everything that isn't the square section
    del lines[0:4]
    for line in lines:
        subList = []
        line = line.rstrip()
        line = line.split(" ")
        subList.append(line[0])
        subList.append(int(line[1]))
        commands.append(subList)
    return commands


def up(square, command):
    '''
    Shifts the column up by 1 index
    :param square: a 3x3 list of lists
    :param command: a list containing a single vertical command "U" and an index
    :return:
    '''


def down(square, command):
    '''
        Shifts the column down by 1 index
        :param square: a 3x3 list of lists
        :param command: a list containing a single vertical command "D" and an index
        :return:
    '''

def left(square, command):
    '''
        Shifts the row left by 1 index
        :param square: a 3x3 list of lists
        :param command: a index for the row
        :return:
    '''
    row = square[command]
    shiftedRow = []

    for x in range(len(row)):
        number = row[x]
        ##the negative indice places the number right before the last element on the
        shiftedRow.insert(-1, number)

    ## replace the row
    square[command] = shiftedRow

    return square

def right(square, command):
    '''
        Shifts the row right by 1 index
        :param square: a 3x3 list of lists
        :param command: a list containing a horizontal command "R" and an index
        :return:
    '''


def makeChanges(square, commands):
    '''

    :param square: a 3x3  list of lists
    :param commands: a list of lists
    :return:
    '''

    for command in commands:
        letter = command[0]
        indice = command[1]

        if letter == "L":
            square = left(square,indice)
        # elif letter == "D":
        #     square = down(square,indice)
        # elif letter == "U":
        #     square = up(square,indice)
        # elif letter == "R":
        #     square = right(square,indice)
    return square

testFile = "torus_2_1.txt"
test_Square = getSquare(testFile)
test_commands = getCommands(testFile)
result = makeChanges(test_Square,test_commands)


print(result)