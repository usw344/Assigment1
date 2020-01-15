def check_diagonals(square):
    '''
    param square: a 3d list containing 9 ints
    return: True if all the diagonals add up to 15. False otherwise
    '''
def check_columns(square):
    '''
    param square: a 3d list containing 9 ints
    return: True if all the columns sum to 15. False otherwiseo
    '''
def check_rows(square):
    '''
    param square: a 3d list containing 9 ints
    return: True if all the rows sum to 15. False otherwise
    '''
def check_range(square):
    '''
    param square: a 3d list containing 9 ints
    return: True if the square contains all the integers 1 .. 9. False otherwise
    '''

### Use these 3 functions
def check_square(square):
    '''
    param square: a 3d list containing 9 ints
    return:True if the square has all the properties of a magic square; False otherwise 
    '''
def get_square():
    '''
    A function to get a list of 9 ints and turns them into a 3d list (3x3). This is done using a nested loop
    return: a 3x3 list of lists
    '''
    rawInput = list( input("Enter 9 integers that are between") )
    aListOfInts = [int(x) for x in rawInput]
    square = []
    for dimension in range(3):
        subList = []
        for element in range(3):
            subList.append( aListOfInts[element] )
        del aListOfInts[:3]
        square.append(subList)
    
    
    return square
def main():
    '''
    '''
    
print(get_square())