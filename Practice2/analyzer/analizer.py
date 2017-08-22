from analyzer.tree import Node

class Analyzer:
    def __init__(self, string):
        self.string = string
        self.tree = None
        self.stack = []

    def analyze(self):
        self.tree = Node()
        current_node = self.tree
        for c in self.string:
            if c == '(':
                node = Node()
                current_node.left = node
                self.stack.append(current_node)
                current_node = current_node.left
            elif c == '|' or c == '.' or c == '*':
                current_node.value = c
                node = Node()
                current_node.right = node
                self.stack.append(current_node)
                current_node = current_node.right
            elif c == ')':
                current_node = self.stack.pop()
            else:
                current_node.value = c
                if self.stack.__len__() > 0:
                    current_node = self.stack.pop()
                else:
                    node = Node()
                    node.left = current_node
                    current_node = node

        self.tree = current_node

    def postorden(self, arbol=None):
        if arbol is None:
            return 0
        self.postorden(arbol.left)
        self.postorden(arbol.right)
        print(arbol.value)

    def create_transition(self, value):
        # meter datos en una pila y si llega un parentesis o una linea o punto sacar de la pila y generar la transicion
