'''
    CS151A
    Project09
    Spring 2021'''

#version 2

#libraries
import sys


class Lsystem:
    def __init__(self, filename = None):
        '''initializes Lsystem object with empty base and rules field'''
        # assign to the field base, the empty string
        self.base = ''
        # assign to the field rules, the empty list
        self.rules = []
        # if the filename variable is not equal to None
        if filename != None:
        # call the read method of self with filename as the argument		
            self.read(filename)
    

    def getBase(self): 
        '''returns lsystem base'''
        # the getBase function should return the value of the base field of the object (self).
        return self.base


    def setBase(self, b): 
        '''sets lsystem base'''
        # the setBase function should assign to the base field (self.base) the value in b.
        self.base = b


    def getRule(self, index): 
        '''returns lsystem rules'''
        # the getRule function should return the specified single rule from the rules field of self.
        return self.rules[index: ]


    def addRule(self, newrule): 
        '''adds new rule to lsystem rules field'''
        # the addRule function should append newrule to the rules field of self.
        self.rules.append(newrule)


    def numRules(self): 
        '''returns number of rules in rules field'''
        # that returns the number of rules in the rules list.
        return len(self.rules)


    def read(self, filename):
        '''opens/reads file and creates lsystem rules and base'''
        # assign to the rules field of self the empty list
        self.rules = []
        # assign to a variable (e.g. fp)file object created w/filename in ‘r’ mode
        fp = open(filename, "r")
        # for each line in fp 
        for line in fp:
            # assign to line the result of calling line.strip()
            line = line.strip()
            # assign variable(e.g.words) as result of calling split() method line
            words = line.split(' ')
            # if the first item in words is equal to the string 'base'
            if words[0] == 'base':
                # call the setBase method of self with the new base string
                Lsystem.setBase(self, words[1])
            # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
                #call addRule method of self w/ new rule(slice of words from index 1
                Lsystem.addRule(self, words[1:])
        # call the close method of the file
        fp.close()


    def replace(self, istring):
        '''creates lsystem string'''
        # assign to a local variable (e.g. tstring) the empty string
        tstring = ''
        # for each character c in the input string (istring)
        for c in istring:
            #print(c+'\n')
            # set a local variable (e.g. found) to False
            found = False
            # for each rule in the rules field of self
            for rule in self.rules:
                # if the symbol in the rule is equal to the character in c
                if rule[0] == c:
                    # add to tstring the replacement from the rule
                    tstring += rule[1]
                    # set found to True
                    found = True
                    # break
                    break
                # if not found
            if found == False:
                # add to tstring the character c
                tstring += c
        # return tstring, make sure this statement is not inside the for loop
        return tstring


    def buildString(self, iterations):
        '''creates lsystem string with certain number of iterations'''
        # assign to a local variable (e.g. nstring) the base field of self
        nstring = self.base
        # for the number of iterations
        for i in range(iterations):
            # assign nstring the result of calling replace method of self w/ nstring as the argument   
            nstring = self.replace(nstring)  
        # return nstring
        return nstring


    def __str__(self):
        '''creates and returns string of lsystem'''
        lsys_string = ''
        # adds base
        lsys_string += 'base ' + self.getBase() +'\n'
        # adds rules
        for i in range(self.numRules()):
            rule = self.getRule(i)
            lsys_string += 'rule ' + str(rule[0][0]) + ' -> ' + str(rule[0][1]) + '\n' 
        return lsys_string

def main(argv):
    '''opens file and prints lsystem'''
    # error message for wrong number of command line arguments
    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()
    # gets file name
    filename = argv[1]
    iterations = 2
    # creates lsystem object
    lsys = Lsystem()
    # calls lsystem methods
    lsys.read( filename )
    lsys.__str__()
    # prints lsystem
    print( lsys )
    
    
if __name__ == "__main__":
    main(sys.argv)
