#mua942
#11275853
#Assigment 1 Question 1
def check_diagonals(square):
    '''
    Checks the diagonals
    param square: a 3d list containing 9 ints
    return: True if all the diagonals add up to 15. False otherwise
    '''

    theSum = 0
    for x in range(3):
        ##because for this down-right diagonal the index of list in the list are the same
        theSum += square[x][x]
    if(theSum != 15):
        return False
    else:
        theSum = 0
        theSum += square[2][0]
        theSum += square[1][1]
        theSum += square[0][2]
        if theSum != 15:
            return False

    return True
def check_columns(square):
    '''
    Checks the same index of each list in the list thus looking at the columns
    param square: a 3d list containing 9 ints
    return: True if all the columns sum to 15. False otherwiseo
    '''
    for indice in range(3):
        ##indice keeps track of which column we are on
        theSum = 0
        for list in square:
            ##this takes the element of the row that is in the column
            ##for example take the 1th element of each row and that is the fisrt colmun
            theSum += list[indice]
        if(theSum != 15):
            return False
    return True
def check_rows(square):
    '''
    Takes a 3x3 list of list and takes the sum of each list in the list and returns false as soon it sees a non-15 value
    param square: a 3d list containing 9 ints
    return: True if all the rows sum to 15. False otherwise
    '''
    for list in square:
        ##a row is a list in the square. sum() gives us the row sum
        if(sum(list) != 15):
            return False

    return True
def check_range(square):
    '''
    Uses a remember-answer boolean list system to check if every number between 1 and 9 are present
    param square: a 3d list containing 9 ints
    return: True if the square contains all the integers 1 .. 9. False otherwise
    '''
    ## a list of 9 Falses
    seen = [False for x in range(9)]

    for dimension in square:
        for element in dimension:
            #Make sure the element is 1-9
            if(element >=1 and element <= 9):
                ##element-1 means that 1-9 number will coorespond to the index of the bool list
                seen[element - 1] = True
            else:
                return False
    if False in seen:
        return False
    else:
        return True



### Use these 3 functions
def check_square(square):
    '''
    calls all the other check functions and returns true if and only if all other function return True. Thus being a Magic Square
    param square: a 3d list containing 9 ints
    return:True if the square has all the properties of a magic square using other functions; False otherwise
    '''
    if not check_range(square):
        return False
    if not check_rows(square):
        return False
    if not check_columns(square):
        return False
    if not check_diagonals(square):
        return False

    return True
def get_square():
    '''
    A function to get a list of 9 ints and turns them into a 3d list (3x3). This is done using a nested loop
    return: a 3x3 list of lists
    '''
    aListOfInts= []
    while len(aListOfInts) != 9:
        raw = int(input("Enter a single positive number"))
        aListOfInts.append(raw)
    square = []

    #dimesnion meanings row in the magic square
    for dimension in range(3):
        subList = []
        for element in range(3):
            subList.append( aListOfInts[element] )
        del aListOfInts[:3]
        square.append(subList)

    return square
def main():
    '''
    This function calls get_square and check_square functions to print YES or NO depending on the return of check_square
    '''
    magicSquare = get_square()
    if(check_square(magicSquare)):
        print("YES")
    else:
        print("NO")


main()