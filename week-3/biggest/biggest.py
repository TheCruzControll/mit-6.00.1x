def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    dict = {}
    for i in aDict:
        dict[i] = len(aDict[i])
    return max(dict)