def print_text():
    print("Welcome to Adder REPL.")
print_text()

def validateVal(val):
    if(val.isalnum()):
        return True
    return False
    
def validateVar(var):
    if var.isalpha():
        return True
    return False
    
def inPut(dic,y):
    dic[y[1]]=input("Enter a value for "+y[1]+": ")
    
def prInt(dic,y):
    if(y[1].isnumeric()):
            print(y[1])
    else:
        try:
            print(y[1]+" equals "+dic[y[1]])
        except:
            print(y[1]+" is undefined.")
            
def gets(dic,y):
    if(not validateVar(y[0])):
        print("Syntax error.")
    elif y[2].isnumeric():
        dic[y[0]]=y[2]
    else:
        try:
            dic[y[0]]=dic[y[2]]
        except:
            print(y[2]+" is undefined.")
            
def adds(dic,y):
    try:
        if(y[2] in dic.keys()):
            dic[y[0]]=str(int(dic[y[0]])+int(dic[y[2]]))
        else:
            print(y[2]+" is undefined.")
    except:
        print(y[0]+" is undefined.")
        
def loop():
    dic={}
    while 1:
        x = input("??? ")
        y = x.split()
        if x == 'quit':
            print('Goodbye.')
            break
        elif(len(y)<=1):
            print("Syntax error.")
        elif(y[0]=='input' and validateVar(y[1])):
            inPut(dic,y)
        elif y[0]=='print' and validateVal(y[1]):
            prInt(dic,y)
        elif y[1]=='gets':
            gets(dic,y)
        elif y[1]=='adds':
            adds(dic,y)
        else:
            print("Syntax error.")
loop()