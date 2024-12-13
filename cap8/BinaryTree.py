class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, subtree):
        self.left = subtree

    def insert_right(self, subtree):
        self.right = subtree

def build_tree(postfix_expr):
    stack = []
    for token in postfix_expr.split():
        if token.isalnum():  # Si es un operando
            stack.append(BinaryTree(token))
        else:  # Si es un operador
            right_subtree = stack.pop()
            left_subtree = stack.pop()
            new_tree = BinaryTree(token)
            new_tree.insert_left(left_subtree)
            new_tree.insert_right(right_subtree)
            stack.append(new_tree)
    if len(stack) != 1:
        raise ValueError("La expresión postfija no es válida.")
    return stack.pop()

def preorder_traversal(tree):
    if tree:
        print(tree.value, end=' ')
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)

def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.left)
        print(tree.value, end=' ')
        inorder_traversal(tree.right)

def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        print(tree.value, end=' ')

# Ejemplos de uso
expressions = [
    "91 95 + 15 + 19 + 4 *",
    "B B * A C 4 * * -",
    "42",
    "A 57",  # Esto debería producir una excepción
    "+ /"   # Esto debería producir una excepción
]

for expr in expressions:
    try:
        print(f"\nExpresión postfija: {expr}")
        tree = build_tree(expr)
        
        print("Recorrido preorden:")
        preorder_traversal(tree)
        
        print("\nRecorrido inorden:")
        inorder_traversal(tree)
        
        print("\nRecorrido postorden:")
        postorder_traversal(tree)
        
    except Exception as e:
        print(f"Error: {e}")