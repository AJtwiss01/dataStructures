#AJ Twiss
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
#got stuck on question #4 unary not finished
def buildParseTree(fpexp):
    fplist = []
    numberinstring = ""
##  This is extending the Build buidParseTree function
##    for loop and checks if its a number and not a math expression 
    for token in fpexp:
        if(token not in ['(','+', '-', '*', '/',')']):
##            if ot a math expresion character it token a string 
            numberinstring = numberinstring + token
##            checks if numbersting does not have a math expression and append to fplist Array
            if token in ['(','+', '-', '*', '/',')']:
                if(numberinstring != ""):
                    fplist.append(numberinstring)
                    numberinstring = ""
                    fplist.append(token)
##    creates a stack
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("((10+5)*3)")
pt.postorder()  #defined and explained in the next section
