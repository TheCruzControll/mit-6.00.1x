def genPrimes():
    x = 1
    p = []
    while True:
        x +=1
        for num in p:
            if (x % num) == 0:
                break
        else:
            p.append(x)
            yield x