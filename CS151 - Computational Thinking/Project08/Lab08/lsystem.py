'''Veer Khosla
CS151 A
Lab 8
lsystem23.py'''

#Version 2
import sys

class Lsystem:
    def __init__(self, filename = None):
        self.base = ''
        self.rules = []
        if filename != None:
            self.read(filename)

    def getBase(self):
        '''sets the L-system base string'''
        return self.base


    def setBase(self, b):
        '''Gets the base string that represents the initial shape'''
        self.base = b


    def getRule(self, index):
        '''adds rule to L-system'''
        return self.rules[index:]


    def addRule(self, newrule):
        '''returns at position index in the L-Lystem'''
        self.rules.append(newrule)

    
    def numRules(self):
        return len(self.rules)
    

    def read(self, filename):
        self.rules = []
        fp = open(filename, 'r')
        lines = fp.readlines()
        for line in lines:
            line = line.strip()
            words = line.split(' ')  
            if words[0] == 'base':
                Lsystem.setBase(self, words[1])
            elif words[0] == 'rule':
                Lsystem.addRule(self, words[1:])
        fp.close()


    def replace(self, istring):
        tstring = ''
        for c in istring:
            found = False
            for rule in self.rules:
                if rule[0] == c:
                    tstring += rule[1]
                    found = True
                    break
            if found == False:
                tstring += c
        return tstring


    def buildString(self, iterations):
        nstring = self.base
        for i in range(iterations):
            nstring = self.replace(nstring)
        return nstring


def main(argv):

    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)

