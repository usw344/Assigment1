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

testFile = "torus_2_1.txt"

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
        :param command: a list containing a single vertical command for up
        :return:
    '''

def right(square, command):
    '''
        Shifts the row right by 1 index
        :param square: a 3x3 list of lists
        :param command: a list containing a single vertical command for up
        :return:
    '''