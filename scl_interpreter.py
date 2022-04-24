
# create an translator for the programming language scl
# the scl_scanner.py and scl_parser.py have already been created, just import them

# Structure:
# Develop translator to intermediate code.
#   Three fundamental components:
#       Program statement
#           *Load and Run
#       Statement
#       Expression Class
# Develop an abstract machine that includes the scanner, parser, and translator.

import scl_scanner as scl_scanner
import scl_parser as scl_parser
import scl_interpreter as scl_interpreter

# print out input list
# TESTING FILE
def scl_translator_printer(fileName):
    for i in fileName:
        print(i)

# type the lexemes
def scl_typing(fileName, keywordsList, identifiersList, operatorsList):
    for i in fileName:
        if i in keywordsList:
            print("Keyword: " + i)
        elif i in identifiersList:
            print("Identifier: " + i)
        elif i in operatorsList:
            print("Operator: " + i)
        else:
            pass

# if i is in keywordsList
def scl_keyword_check(i, filelist):
    # if i is in keywordsList is 'import'
    if i == 'import':
        print("imported" + filelist[i+1])
    elif i == 'run':
        print("run")
    elif i == 'load':
        print("load" + filelist[i+1])
    # if i is in keywordsList is a type
    elif i == 'struct' | 'double' | 'char' | 'float' | 'long' | 'short' | 'bool' :
        # get the variable next to the type
        print("type: " + i + " " + filelist[i+1])
        
def