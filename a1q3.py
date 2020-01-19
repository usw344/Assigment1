##Muhammad Usman Ahmed
##mua942
##11275853
#CMPT145 LO2
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
        #take away end of line space
        line = line.rstrip()

        #split list by space or when line ends
        line = line.split(" ")

        ##take the "line" which is a list of numbers in str form and turn it into a list of ints
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

        #clean away end of line which has a space
        line = line.rstrip()

        #split at each line
        line = line.split(" ")

        ## first append the Letter-command as a string
        subList.append(line[0])

        ##then take the index and convert as int int temp-sublist
        subList.append(int(line[1]))


        commands.append(subList)
    return commands


def up(square, command):
    '''
    Shifts the column up by 1 index
    :param square: a 3x3 list of lists
    :param command: an index to run on
    :return: the shifted square
    '''
    col = []
    for list in square:
        ## to get the nth column we have to take that same index of the row
        col.append(list[command])

    ## up turns our to be a left ward shift on the column
    shiftedCol = []
    for x in range(len(col)):
        number = col[x]

        ##the negative indice places the number right before the last element on the list.
        shiftedCol.insert(-1, number)

    ##put the values back into the square
    for y in range( len(square) ):
        square[y][command] = shiftedCol[y]


    return square

def down(square, command):
    '''
        Shifts the column down by 1 index
        :param square: a 3x3 list of lists
        :param command: an index to run on
        :return: the shifted square.
    '''
    col = []
    for list in square:
        ## to get the nth column we have to take that same index of the row
        col.append( list[command]  )

    ##now shift it down by one. This turns out to be a right ward shift down on the column
    shiftedCol = []
    for x in range( len(col)-1,-1,-1   ):
        number = col[x]
        shiftedCol.insert(1,number)


    ##now make changes to the square
    for y in range( len(square) ):
        square[y][command] = shiftedCol[y]


    return square

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

        ##the negative indice places the number right before the last element on the list.
        shiftedRow.insert(-1, number)

    ## replace the row
    square[command] = shiftedRow

    return square

def right(square, command):
    '''
        Shifts the row right by 1 index
        :param square: a 3x3 list of lists
        :param command: and index to work on
        :return:
    '''
    row = square[command]
    shiftedRow = []

    for x in range( len(row)-1, -1,-1 ):
        number = row[x]

        ##add the value right after 0th element. Thus shifting everthing to the right
        shiftedRow.insert(1, number)

    ##replace the row
    square[command] = shiftedRow

    return square





def makeChanges(square, commands):
    '''
    goes through the command lst and first determines the command-type and then takes the index and calls the correct change function
    :param square: a 3x3  list of lists
    :param commands: a list of lists
    :return:
    '''

    for command in commands:
        letter = command[0]
        indice = command[1]

        if letter == "L":
            square = left(square,indice)
        elif letter == "D":
            square = down(square,indice)
        elif letter == "U":
            square = up(square,indice)
        elif letter == "R":
            square = right(square,indice)
    return square


def main(fileName):
    '''
    A main function that calls all other functions
    :param fileName: a string containing the name a file in dir
    :return: the final 3x3 configuration
    '''
    test_Square = getSquare(fileName)
    test_commands = getCommands(fileName)
    result = makeChanges(test_Square, test_commands)

    return result


##this could be any name
file = "torus.txt"
print(main(file))