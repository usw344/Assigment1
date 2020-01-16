from builtins import range


def check_diagonals(square):
    '''
    param square: a 3d list containing 9 ints
    return: True if all the diagonals add up to 15. False otherwise
    '''
def check_columns(square):
    '''
    Checks the same index of each list in the list thus looking at the columns
    param square: a 3d list containing 9 ints
    return: True if all the columns sum to 15. False otherwiseo
    '''
    for indice in range(3):
        theSum = 0
        for list in square:
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
    param square: a 3d list containing 9 ints
    return:True if the square has all the properties of a magic square using other functions; False otherwise
    '''
    if check_range(square) or check_rows(square) or check_columns(square):
        return True

    return True ## later will return False when the other functions work
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
    print(magicSquare)
    if(check_square(magicSquare)):
        print("YES")
    else:
        print("NO")


main()