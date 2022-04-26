import scl_scanner
import scl_lexier
import Old.scl_interpreterOld as scl_interpreterOld

import os


# open files that are inside the source folder and read

keywordsCheck = scl_scanner.keywordScanner()
operatorsCheck = ['=', '*', '/', '('')', '[]', '<=', ":"]
identifiersCheck = scl_scanner.identifierScanner()
identifierDuplicate = []
fileName = ''

def compiler():
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

#menu system to access all parts of parser
class parserMenu():

    def printMenu():
        global fileName
        print("========Menu========")
        print("1) Choose File ")
        print("2) Read File")
        print("3) Scan File")
        print("4) Parse File")
        print("5) Run Translator")
        print("6) Exit ")
        print("====================")

        #user input to navigate menu
        choice = input()
        if choice == '1':
            fileName = parserMenu.chooseFile()
            compiler()
            parserMenu.printMenu()
        elif choice == '2':
            if fileName == '':
                print("\nPlease select a file first")
                parserMenu.printMenu()
            parserMenu.readFilename()
            parserMenu.printMenu()
        elif choice == '3':
            if fileName == '':
                print("\nPlease select a file first")
                parserMenu.printMenu()
            global keywordsList
            global identifiersList
            global operatorsList
            keywordsList, identifiersList, operatorsList = parserMenu.scanFile()
            parserMenu.printMenu()
        elif choice == '4':
            if fileName == '':
                print("\nPlease select a file first")
                parserMenu.printMenu()
            parserMenu.begin()
            parserMenu.printMenu()
        elif choice == '5':
            print(keywordsList, identifiersList, operatorsList) 
            if fileName == '':
                print("\nPlease select a file first")
                parserMenu.printMenu()
            translate()
            # put translator here...
        elif choice == '6':
            print("Exiting....")
        else:
            print("Wrong Choice, Try Again")

    #choose scl file in working directory to use
    def chooseFile():
        global fileName
        sclFiles = []
        counter = 1
        files = os.listdir(os.getcwd())
        print("\nPlease put scl files in working directory and press the number for the file you would like to open:")
        for scl in files:
            if ".scl" in scl:
                print("[" + str(counter) + "] " + scl)
                sclFiles.append(scl)
                counter += 1
        choice = input()
        fileNum = int(choice) - 1
        fileName = sclFiles[fileNum]
        return(fileName)

    #reads file 
    def readFilename():
        # open files that are inside the source folder and read
        print(scl_scanner.read(fileName))
        print("\n===============================")
        print("   End of File Name: " + fileName)
        print("===============================\n")


    def scanFile():
        global keywordsCheck
        global identifiersCheck
        global operatorsCheck
        readSCL = scl_scanner.read(fileName)
        cleanedText = scl_scanner.cleanup(readSCL)
        keywordsCheck = scl_scanner.keywordScanner()
        identifiersCheck = scl_scanner.identifierScanner()
        operatorsCheck = scl_scanner.operatorScanner()
        scl_scanner.displayKeywords()
        scl_scanner.displayIdentifiers()
        scl_scanner.displayOperators()
        return keywordsCheck, identifiersCheck, operatorsCheck

    def begin():
        start()



def start():
    index = 0
    indexAhead = index + 1
    scl = compiler()
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

def translate():
    print("Translating...")
    scl = compiler()
    scl_interpreterOld.scl_translator_printer(scl)

parserMenu.printMenu()



    