#bit swap
def swapBits(x, p1, p2, n):

    # Move all bits of first
    # set to rightmost side
    set1 = (x >> p1) & ((1 << n) - 1)
    print(set1)

    # Move all bits of second
    # set to rightmost side
    set2 = (x >> p2) & ((1 << n) - 1)
    print(set2)

    # XOR the two sets
    xor = (set1 ^ set2)
    print(xor)

    # Put the xor bits back
    # to their original positions
    xor = (xor << p1) | (xor << p2)
    print(xor)

    # XOR the 'xor' with the
    # original number so that the
    # two sets are swapped
    #result = x ^ xor
    #print(result)

    return xor
res=swapBits(6,0,2,1)
print(res)