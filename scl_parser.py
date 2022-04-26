import scl_lexier 
import scl_scanner 


# open files that are inside the source folder and read
keywordsCheck = scl_scanner.keywordScanner()
operatorsCheck = ['=', '*', '/', '('')', '[]', '<=', ":"]
identifiersCheck = scl_scanner.identifierScanner()
identifierDuplicate = []
fileName = ''

def compiler(fileName):
    readSCL = scl_scanner.read(fileName)
    cleanedText = scl_scanner.cleanup(readSCL)
    return cleanedText

#keyword function
def keywords(text, nextword):
    print("<ENTERING KEYWORDS>")
    if text in keywordsCheck:
        
        if nextword or "EOF" in identifiersCheck:
            print("<RETUNRING KEYWORDS>")
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print("<RETUNRING KEYWORDS>")
        return

#get identifier
def identifier(text, nextword):
    print("<ENTERING IDENTIFIERS>")
    identifierExists(text, nextword)
    if text in identifiersCheck:
        if nextword or "EOF" in operatorsCheck:
            print('<RETURNING IDENTIFIERS>')
            return
        elif nextword in keywordsCheck:
            print('<RETURNING IDENTIFIERS>')
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print('<RETURNING IDENTIFIERS>')
        return

#check for identifier duplications
def identifierExists(text, id):
    if text == 'define':
            identifierDuplicate.append(id)
            if id in identifierDuplicate:
                print('SYNTAX ERROR!')

 # get operators
def operators(text, nextword):
    print("<ENTERING OPERATORS>")
    if text in operatorsCheck:
        if nextword or "EOF" in identifiersCheck:
            print("<RETURNING OPERATORS>")
            return
        else:
            print('SYNTAX ERROR!')
    else:
        print('<RETURNING IDENTIFIERS>')
        return
    
#display syntax error
def syntaxError():
    print('SYNTAX ERROR')




def startParse(fileName):
    index = 0
    indexAhead = index + 1
    scl = compiler(fileName)
    scl.append("EOF")

    for each in scl:
        Token, Lexeme = scl_lexier.lex(each)
        keywords(scl[index], scl[indexAhead])
        identifier(scl[index], scl[indexAhead])
        operators(scl[index], scl[indexAhead])
        index += 1
        indexAhead = index + 1
        if indexAhead >= len(scl):
            break





    