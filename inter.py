#!/usr/bin/env python
# coding: utf-8

# In[17]:


class AbstractSyntaxTree:
    def __init__(self, block = None):
        self.block = block # BasicBlock
        self.variables = {} # словарь: символ переменной - ее значение
    def oper(self):
        self.block.oper(self.variables)
        return self.variables['result']

class Assign:
    def __init__(self, k = "", cond = None):
        self.k = k
        self.cond = cond
    def oper(self, variables):
        variables[self.k] = self.cond.oper(variables)
    
class Block: # подается на вход дерева
    def __init__(self, list_of_assign = None):
        self.list_of_assign = list_of_assign
    def oper(self, variables):
        for x in self.list_of_assign:
            x.oper(variables)

# операции в языке +, -, *, >, <, ==
            
class Expr:
    def __init__(self, value = None, op = None, cond = None):
        self.value = value
        self.cond = cond
        self.op = op
    def oper(self, variables = None):
        a = self.value
        if a in variables:
            a = variables[self.value]
        if self.op is None:
            return a
        b = self.cond.oper(variables)
        if self.op == '+':
            return a + b
        elif self.op == '-':
            return a - b
        elif self.op == '*':
            return a * b
        elif self.op == '>':
            return a > b
        elif self.op == '<':
            return a < b
        else:
            return a == b


# In[20]:


#Example
a1 = Assign('a', Expr(43))
a2 = Assign('b', Expr(33))
b1 = Expr("a", "-", Expr("b")) 
a3 = Assign("c", Expr(24))
b2 = Expr("c", "*", b1)
a4 = Assign('result', b2)
block0 = Block([a1, a2, a3, a4])

tree = AbstractSyntaxTree(block0)
print(tree.oper())


# In[ ]: 240




