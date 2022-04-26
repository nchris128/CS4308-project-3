
import scl_interpreter
import scl_lexier 
import scl_scanner 
import scl_parser 
import os

def printMenu():
    global fileName
    
    print("========Menu========")
    print("1) Choose File ")
    print("2) Read File")
    print("3) Scan File")
    print("4) Parse File")
    print("5) Interpret File")
    print("6) Exit ")
    print("====================")

    #user input to navigate menu
    choice = input()
    if choice == '1':
        fileName = chooseFile()
        scl_parser.compiler(fileName)
        printMenu()
    elif choice == '2':
        if fileName == '':
            print("\nPlease select a file first")
            printMenu()
        readFilename()
        printMenu()
    elif choice == '3':
        if fileName == '':
            print("\nPlease select a file first")
            printMenu()
        scanFile()
        printMenu()
    elif choice == '4':
        if fileName == '':
            print("\nPlease select a file first")
            printMenu()
        begin(fileName)
        printMenu()
    elif choice == '5':
        if fileName == '':
            print("\nPlease select a file first")
            printMenu()
        scl_interpreter.interpreter()
        printMenu()
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

def begin(fileName):
    scl_parser.startParse(fileName)

printMenu()