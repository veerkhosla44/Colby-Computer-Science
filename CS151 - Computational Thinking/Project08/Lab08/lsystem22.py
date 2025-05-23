'''lsystem22.py
Converts L-System string into turtle commands
CS151 Visual Media, Fall 2022
'''
# has functions: init / setBase / getBase / addRule / getRule
import sys


def init():
    '''returns an empty L-system'''
    return ['',[]]

def setBase( lsys, base):
    '''sets the L-system base string'''
    lsys[0] = base


def getBase(lsys):
    '''Gets the base string that represents the initial shape'''
    return lsys[0]


def addRule(lsys, rule):
    '''adds rule to L-system'''
    lsys[1].append(rule)


def getRule(lsys, ruleIdx):
    '''returns at position index in the L-Lystem'''
    return lsys[1][ruleIdx]


def getFindStr(lsys):
    '''Gets the symbol in the replacement rule that we find to replace'''
    return lsys[1][0]


def getReplaceStr(lsys):
    '''Gets the replacement string in the replacement rule'''
    return lsys[1][1]


def createLsystemFromFile(filename):
    """ Create an L-system list by reading in the specified file """
    lsys = init()
    fp = open(filename, 'r')
    lines = fp.readlines()
    fp.close()
    for line in lines:
        line = line.strip()
        words = line.split()
        if words[0] == 'base':
            setBase(lsys, words[1])
        else:
            addRule(lsys, words[1:])
    return lsys

def buildString(lsys, n):
    """ Return a string generated by applying the L-system rules  
        n times"""
    nstring = getBase(lsys)
    symbol, replacement = getRule(lsys, 0)
    for i in range(n):
        nstring = nstring.replace(symbol, replacement)
    return nstring

        
    # L3 test 
#def main():
    # my_lsys = init()
    #lsys_filename = argv[2]
    # lsys = createLsystemFromFile(lsys_filename)
    # print(lsys)
    # my_lsys = init()
    # setBase( my_lsys, 'A' )
    # addRule( my_lsys, ['A','AB'] )
    # print(my_lsys)
    # print("the base is ", getBase( my_lsys ))
    # print("the first rule is ", getRule( my_lsys, 0 ))
    # # code to test reading from a file
#if __name__ == '__main__':
    #main()

    #L5 test
# def main(argv):
#     '''prints out rule and base of L-system'''
#     if len(argv) < 2:
#         print("Usage : python3 lsystem.py <filename>")
    #lsys_filename = argv[1]
    #lsys = createLsystemFromFile(lsys_filename)
    #print(lsys)
    # L5 test python3 lsystem22.py systemA1.txt
    # L5 test python3 lsystem22.py systemA2.txt

#if __name__ == '__main__':
    #main(sys.argv)

    #L6 test
def main(argv):
    if len(argv) < 3:
        print("Usage : python3 lsystem.py <in_filename><num_iterations>")
        exit()

    lsys_filename = argv[1]
    lsys = createLsystemFromFile( lsys_filename )
    print(lsys)
                                         
    num_iter = int(argv[2] )
    s = buildString(lsys, num_iter )
    print(s)

if __name__ == "__main__":
    main(sys.argv)



#     # define number of iteration, distance, angle
#     nItr = 4
#     dist = 10
#     angle = 60

#     # Define our L-System base string and production rule
#     baseStr = 'F--F--F'
#     findStr = 'F'
#     replaceStr = 'F+F--F+F'
#     lsystem = [baseStr, [findStr, replaceStr]]

#     # Apply our rule n times
#     iteratedStr = makeIteratedString(lsystem, nItr)

#     # Have turtle draw the shape represented by the L-System string
#     drawString(iteratedStr, dist, angle)

#     # Print out the final iterated L-System string
#     print(iteratedStr)

# if __name__ == '__main__':
#     turtle.tracer(False)
#     main()
#     turtle.update()
#     turtle.exitonclick()
#     # input('Press any key to exit...')