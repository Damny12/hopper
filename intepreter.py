import sys
code = input("Type in your file's name:")
try:
    file = open(code)
except:
    print("This file doesn't exist")
    sys.exit("Invalid file")
code = file.read()
codeLines = code.splitlines()
currentLine = 0
varNames = []
varValues = []

def check(currentLine=int):
    line = codeLines[currentLine]
    global newLine
    newLine = currentLine+1
    output=""
    pointer=0
    if "hop(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if int(output) > len(codeLines) or int(output) < 0:
            print("This is an invalid line!")
            sys.exit("Invalid line")
        else:
            newLine=int(output)
    if "print(" in line:
        pointer = line.index("(") +1
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        print(output)
    if "var(" in line:
        pointer = line.index("(") +1
        while line[pointer] != "=":
            output+=line[pointer]
            pointer+=1
        varNames.append(output)
        pointer = line.index("=") +1
        output=""
        while pointer < len(line)-1:
            output+=line[pointer]
            pointer+=1
        try:
            output = int(output)
            varValues.append(output)
        except:
            varValues.append(output)    
    print(varNames,varValues)

while currentLine < len(codeLines):
    check(currentLine)
    currentLine=newLine