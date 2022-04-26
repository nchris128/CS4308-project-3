import scl_lexier
import scl_scanner

lexemeList = scl_lexier.lexemeList
tokenList = scl_lexier.tokenList
interpreterArr = []
# store variables in a dictionary
variables = {}
idx = 0

def interpreter():
    for lexeme in lexemeList:
       
        if lexeme == 'import':
            inter_imports()

        elif lexeme == 'define':
            inter_declare()

        # if lexeme == 'set':
        #     inter_set()

        elif lexeme == 'function':
            inter_func()

        idx =+ 1
    for each in interpreterArr:
        print(each)
    print("\n ============= END OF FILE =============")
    

def inter_imports():
    if '.h' in lexemeList[idx+1] and tokenList[idx] == 11:
        interpreterArr.append('import ' + lexemeList[idx+1])
    return

def inter_declare():
    if lexemeList[idx+1] in scl_scanner.identifiterList:
        interpreterArr.append(lexemeList[idx+1] + " = " + lexemeList[idx+2])  
    return

# def inter_set():
#     # set is equivalent to stating a variable
#     # ergo set x = 5 is equivalent to x = 5 in python
#     # turn set x = 5 into x = 5
#     if 

def inter_func():
    if type(lexemeList[idx+1]) == str:
        interpreterArr.append("def " + lexemeList[idx+1])
    return  
def test():
    print(len(lexemeList))
    print(len(tokenList))