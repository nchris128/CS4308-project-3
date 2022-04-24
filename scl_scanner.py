import re
#removing comments and unnecessary symbols
cleanedSCL = []

def cleanup(scl):
    global cleanedSCL
    cleanedText = ''
    #characters to remove from code
    # toStrip = ',.":'

    #replacing each instance of the character with spaces
    # for toStrip in toStrip:
    #     strippedText = scl.replace(toStrip, ' ')

    #split the code into a list of lines

    space = re.compile(r"([()])")
    spaceText = space.sub(' \\1 ', scl)

    lineText =  spaceText.splitlines()
    descriptionIndex = 0
    lineText = [i.lstrip() for i in lineText]

    for descriptionLine in lineText:
        #finding lines with description
        if 'description' in descriptionLine.lstrip():
            descriptionIndex = lineText.index('description')

            #remove lines until */ is found
            while '*/' not in lineText[descriptionIndex]:
                descriptionLine = lineText.pop(descriptionIndex)

            #else to remove the leftover end comment
            else:
                descriptionLine = lineText.pop(descriptionIndex)

    #removing single line comments by creating a substring before //
    for line in lineText:
        if '//' in line:
            index = line.index('//')
            cleanedText = cleanedText + line[0:index] + '\n'
        else:
            cleanedText = cleanedText + line + '\n'
    cleanedSCL = cleanedText.split()
    return(cleanedSCL)


def keywordScanner():
    # global keywordList
    #table for keywords to compare to the scl file
    keywordTable =['import', 'begin', 'call','using', 'endfun', 'set', 'exit',
                 'symbol', 'forward', 'function', 'parameters', 'array', 'integer',
                 'struct', 'double', 'Serial.println', 'char', 'float', 'byte', 'display', 'while', 'endwhile',
                 'unsigned', 'long', 'short', 'definetype', 'forward', 'return', 'type', 'void', 'parameters',
                 'pointer', 'DataT', 'listT', 'nodePtrT', 'address', 'using', 'destroy', 'NodeType', 'variables',
                 'parameters', 'bool']
    keywordList = []

    #iterates through scl to find keywords and add it to new list
    for i in cleanedSCL:
        if i in keywordTable:
            keywordList.append(i)

    return(keywordList)
 
def identifierScanner():
    # global identifiterList
    #iterates through scl looking for identifiers being defined then adding to new list
    idx = 0
    identifiterList = []
    for i in cleanedSCL:
        idx += 1
        if i == 'define':
            identifiterList.append(cleanedSCL[idx])

    return(identifiterList)

def operatorScanner():
    # global operatorList
    #iterates through scl to find operators and add it to new list
    operatorTable = [ '=', '*', '/', '(', ')', '[]', '<=', '>=', ':']
    operatorList = []
    for i in cleanedSCL:
        if i in operatorTable:
            operatorList.append(i)

    return(operatorList)

def displayKeywords():
    keywordList = keywordScanner()
    print('\nKeywords Found:')
    print(keywordList)
    print('Keywords Total: ' + str(len(keywordList)))  

def displayOperators():
    operatorList = operatorScanner()
    print('\nOperators Found:')
    print(operatorList)
    print('Operators Total: ' + str(len(operatorList)))  

def displayIdentifiers():
    identifiterList = identifierScanner()
    print('\nIdentifiers Found:')
    print(identifiterList)
    print('Identifiers Total: ' + str(len(identifiterList)))  

def read(fileName):
    # print('Please enter the name for the scl file to scan\nExample: arduino_ex1.scl')
    # file = input()
    file = fileName
    try:
        openedFile = open(file)
        scl = openedFile.read()
        return scl
    except(FileNotFoundError, UnboundLocalError):
        print("Please select a file first")

    
#user enters scl location to scan then is opened to read
# scl = read(Menu.chooseFile())
# keywordScanner()
# identifierScanner()
# operatorScanner()
# print(cleanup())


