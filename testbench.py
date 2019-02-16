def pb(csp):
    for i in range(csp.n):
        for j in range(csp.n):
            if (csp.queens[j] != i):
                print(" ", end = '|')
            else:  print(j, end = '|')
        print("")
def pc(csp):
    print("Conflicts:")
    for i in csp.queens:
        print("Queen " + str(i) + ": " + str(i.conflicts))


def confirmSolution(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if (j != i):
                if (s[j] == s[i] or
                    s[j] == s[i] + j - i or
                    s[j] == s[i] - j + i):

                    print("Found error, Queen " +
                          str(i) + " conflicts with " + str(j))
                    return False
    return True



##with open("nqueens.txt", 'w+') as f:
##    f.writelines([])

from cisc352Final import *
import timeit


##for i in range (4, 1500):
##    s = runAlgorithm(i)
##    if(not confirmSolution(s)):
##                print(s)
##                break
##    else: print("correct at " + str(i) + " = n.")



for i in range(4,1000000, 9363):
    print(timeit.timeit("runAlgorithm("+str(i)+")",
                        "from cisc352Final import runAlgorithm", number = 1))
    
                
