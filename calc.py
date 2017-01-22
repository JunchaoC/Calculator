#convert input into buffer type for more convenient handle of string 
class Buffer(object):
    def __init__(self,data):
        self.data = data
        self.offset = 0

    #return char in current position
    def peek(self):
        if self.offset >= len(self.data):
            return None

        return self.data[self.offset]

    #move current position by 1
    def advance(self):
        self.offset += 1


#define token parent type
class Token(object):
    def consume(self, buffer):
        pass

#define class intToken and optToken that inherit classToken 
class intToken(Token):
    #get a number from buffer adn return a (type,number) tuple
    def consume(self, buffer):
        tok = ""
        while True:
            ch = buffer.peek()
            if ch is not None and ch.isdigit():
                tok += ch
                buffer.advance()
            else:
                break
        
        if tok != "":
            return ("int",int(tok))
        else:
            return None

class optToken(Token):
    #get a operator from buffer and return a (type,operator) tuple
    def consume(self, buffer):
        while True:
            ch = buffer.peek()
            if ch is not None and ch in "+-":
                buffer.advance()
                return ("ope",ch)
            else:
                return None


#Retrieve number and operator from input
def tokenize(string):
    buf = Buffer(string)
    intTok = intToken()
    optTok = optToken()
    tokens = []

    while buf.peek():
        token = None
        for tk in (intTok, optTok):
            token = tk.consume(buf)
            if token:
                tokens.append(token)
                break

        if not token:
            raise ValueError("Error in syntax")

    return tokens


class Node(object):
    pass

#define two child type intNode and optNode  that inherit type Node for claculation
class intNode(Node):
    def __init__(self, value):
        self.value = value

class optNode(Node):
    def __init__(self, opt):
        self.opt = opt
        self.left = None
        self.right = None

#parse the input string in to binary tree
def parse(tokens):
    if tokens[0][0] != "int":
        raise ValueError("Must start with an integer")

    prev_node = intNode(tokens[0][1])
    curr_node = None
    prev = "int"

    for token in tokens[1:]:
        #Error if two neighboring node are of same type
        if token[0] == prev:
            raise ValueError("Error in syntax")
        prev = token[0]

        #if token is operator, set left child to previous node
        if token[0] == 'ope':
            curr_node = optNode(token[1])
            curr_node.left = prev_node

        #if token is int, the node is a leaf in the tree
        if token[0] == 'int':
            curr_node.right = intNode(token[1])
            prev_node = curr_node

    return curr_node

def calculate(curr_node):
    #traverse down to the leftmost leaf
    if isinstance(curr_node.left, optNode):
        left_val = calculate(curr_node.left)
    else:
        left_val = curr_node.left.value

    #calculate sum/difference of curr_node's children
    if curr_node.opt == '+':
        return left_val + curr_node.right.value
    elif curr_node.opt == '-':
        return left_val - curr_node.right.value
    else:
        raise ValueError("Wrong operator")




if __name__ == '__main__':
    input = raw_input('Input:')
    tokens = tokenize(input)
    node = parse(tokens)
    print("Result: " + str(calculate(node)))    
#print(tokens)
