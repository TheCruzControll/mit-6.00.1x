def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if len(aStr) == 0:
        return False
        
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    elif len(aStr)==1:
        return False
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])