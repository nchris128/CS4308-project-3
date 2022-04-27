import scl_lexier
import scl_scanner

lexemeList = scl_lexier.lexemeList
tokenList = scl_lexier.tokenList
interpreterArr = []

# store variables in a dictionary
variables = {}


def interpreter():
    print("====================\n")
    global idx
    global arrType
    idx = 0
    arrType = ''
    for lexeme in lexemeList:
        

        if lexeme == 'import':
            inter_imports()

        elif lexeme == 'define':
            inter_declare()

        elif lexeme == 'symbol':
            inter_symbol()

        elif lexeme == 'set':
            inter_set()

        elif lexeme == 'display':
            inter_display()

        elif lexeme == 'while':
            inter_while()
            
        elif lexeme == 'for':
            inter_for()

        elif lexeme == 'endfor':
            inter_endfun()

        elif lexeme == 'function':
            inter_func()

        elif lexeme == 'destroy':
            pass
        
        elif lexeme == 'call':
            inter_call()

        elif lexeme == 'endfun':
            inter_endfun()

        idx = idx + 1
    indent()
    for each in interpreterArr:
        print(each)
    print("\n ============= END OF FILE =============")
    

def inter_imports():
    if '.h' in lexemeList[idx+1] and tokenList[idx] == 11:
        interpreterArr.append('import ' + lexemeList[idx+1])
    return

def inter_declare():
    if lexemeList[idx+1] in scl_scanner.identifiterList and lexemeList[idx+2] == '=':
        interpreterArr.append(lexemeList[idx+1] + " = " + lexemeList[idx+3])  
    else:
        # removes the type
        interpreterArr.append(lexemeList[idx+1] + " = " + "None")
    return

def inter_symbol():
    if lexemeList[idx+1] in scl_scanner.identifiterList:
        interpreterArr.append(lexemeList[idx+1] + " = " + "hex(0x" + lexemeList[idx+2] + ")")

def inter_set():
    # set is equivalent to stating a variable
    if lexemeList[idx+1] in scl_scanner.identifiterList:
        # append the variable name and the value into variables list
        variables[lexemeList[idx+1]] = lexemeList[idx+2]
        
        j = 3
        expression = ''
        while lexemeList[idx+j] not in scl_scanner.keywordTable:
            expression = expression + lexemeList[idx+j] + " "
            j = j + 1
        interpreterArr.append(lexemeList[idx+1] + " = " + expression)
    return

def inter_display():
    j = 1
    display = ''
    while lexemeList[idx+j] not in scl_scanner.keywordTable:
        display = display + lexemeList[idx+j] + " "
        j = j + 1
    interpreterArr.append("print(" + lexemeList[idx+1] + " = " + display + ")")
        

def inter_while():
    # append while to the interpreterArr
    j = 1
    whileValues = ''
    while lexemeList[idx+j] != 'do':
        whileValues = whileValues + lexemeList[idx+j] + " "
        j = j + 1
    interpreterArr.append("while " + whileValues + ":")
    return

def inter_for():
    interpreterArr.append("for " + lexemeList[idx+1][0] + " in" + lexemeList[idx + 6])
    j = 0
    forVar = ''
    while lexemeList[idx+j] not in scl_scanner.keywordTable:
        forVar = forVar + lexemeList[idx+j] + " "
        j = j + 1
    
def inter_func():
    
    global arrType
    if type(lexemeList[idx+1]) == str and lexemeList[idx+2]:
        interpreterArr.append("def " + lexemeList[idx+1] + ":")
        
        if lexemeList[idx+2] == 'return':
            arrType = lexemeList[idx+4]
        else:
            arrType = ""
    return  

def inter_endfun():
    # if arrType != '':
    #     interpreterArr.append(arrType)
    # else: 
    interpreterArr.append("return")

    return

def inter_call():
    interpreterArr.append(lexemeList[idx+1] + '(' +lexemeList[idx+3] + ')')
    return

# def inter_return():
#     arrType = 
#     # interpreterArr.append("return " + lexemeList[idx+1])
#     return

#checks if the line requires an indent 
def indent():
    indentCount = 0
    index = 0
    for i in interpreterArr:
        if "def" in interpreterArr[index - 1] or "for" in interpreterArr[index - 1] or "while" in interpreterArr[index - 1]:
            indentCount = indentCount + 1
        elif "return" in interpreterArr[index - 1]:
            indentCount = indentCount - 1
        if indentCount == 1:
            interpreterArr[index] = "    " + i
        elif indentCount == 2:
            interpreterArr[index] = "       " + i
        elif indentCount == 3:
            interpreterArr[index] = "          " + i    
            
        index = index + 1

def test():
    print(len(lexemeList))
    print(len(tokenList))