import math

awn = None

def setAwn(val):
    
    global awn
    awn = val


def execute(string):

    global awn

    python = "setAwn( "
    instructions = []
    instr = ""

    for char in string:

        if char == ' ':

            if instr == "multiplied" or instr == "divided" or instr == "to" or instr == "to the" or instr == "to the power" or instr == "open" or instr == "close": # """or instr == 'to the root'"""
                
                instr += char
            
            else:
                
                instructions.append(instr)
                instr = ""
        
        else:
        
            instr += char
        
    instructions.append(instr)

    for instruction in instructions:

        if instruction == "add" or instruction == "plus":
            
            python += ' + '

        elif instruction == "multiplied by" or instruction == "times" or instruction == "x":
            
            python += ' * '

        elif instruction == "divided by":
            
            python += ' / '

        elif instruction == "subtruct" or instruction == "minus":
            
            python += ' - '

        elif instruction == "to the power of" or instruction == "^":
            
            python += ' ** '

        elif instruction == "root":

            python += " math.sqrt "

        #elif instruction == "to the root of":
        #    
        #    pass

        elif instruction == "over":
            
            python += ' / '

        elif instruction == "open parenthesis":
            
            python += ' ( '

        elif instruction == "close parenthesis":
            
            python += ' ) '

        else:

            python += instruction
    
    c = compile(python + ')', "math.py", "exec")
    try:
        exec(c)
    except:
        pass

    return awn