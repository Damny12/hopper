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
    if "//" in line:
        currentLine+=1
        return 
    if "set(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory = varNames.index(output)
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            varValues[memory] = int(output)
        except:
            varValues[memory] = output
    if "pow(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory = varNames.index(output)
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            varValues[memory] = pow(varValues[memory],int(output))
        except:
            print("This is not a number.")
            sys.exit("Invalid type")
    if "div(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory = varNames.index(output)
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            varValues[memory] /= int(output)
        except:
            print("This is not a number.")
            sys.exit("Invalid type")
    if "mult(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory = varNames.index(output)
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            varValues[memory] *= int(output)
        except:
            print("This is not a number.")
            sys.exit("Invalid type")
    if "add(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory = varNames.index(output)
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            varValues[memory] += int(output)
        except:
            varValues[memory] += output
    if "input(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ",":
            output+=line[pointer]
            pointer+=1
        pointer = line.index(",")+1
        memory=output
        output = ""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        varNames.append(output)
        try:
            memory = int(input(memory))
        except:
            print("no num")
        varValues.append(memory)
        
    if "hop(" in line:
        pointer = line.index("(")+1
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
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
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        print(output)
    
    if "var(" in line:
        pointer = line.index("(") +1
        while line[pointer] != "=":
            output+=line[pointer]
            pointer+=1
        varNames.append(output)
        pointer = line.index("=") +1
        output=""
        while line[pointer] != ")":
            output+=line[pointer]
            pointer+=1
        if "!" in output:
            output = varValues[varNames.index(output.lstrip("!"))]
        try:
            output = int(output)
            varValues.append(output)
        except:
            varValues.append(output)  

while currentLine < len(codeLines):
    check(currentLine)
    currentLine=newLine