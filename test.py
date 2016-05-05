def readText():
    f = []
    f = open('s.txt').read().split('\n')
    f.reverse()
    for i in f:
        j = i+'\n'
    print(j)
readText()