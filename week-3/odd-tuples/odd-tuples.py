def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    tup = ()
    for i in aTup[:len(aTup):2]:
        tup = tup+(i,)
    return tup