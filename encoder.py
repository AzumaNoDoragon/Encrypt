def hashing():
    alfnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    transHash = [["" for _ in range(36)] for _ in range(36)]

    for i in range(36):
        for j in range(36):
            index = i + j
            if(index >= 36):
                index = index - 36
            transHash[i][j] = alfnum[index]
    return transHash

transHash = hashing()