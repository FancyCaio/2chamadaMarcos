#Aluno: Caio Henrique Araújo Silva Braga

import json
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def pre_order_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result.extend(pre_order_traversal(root.left))
        result.extend(pre_order_traversal(root.right))
    return result
def post_order_traversal(root):
    result = []
    if root:
        result.extend(post_order_traversal(root.left))
        result.extend(post_order_traversal(root.right))
        result.append(root.val)
    return result
with open('arvore.json', 'r') as file:
    data = json.load(file)
    values = data['values']
bst_root = None
for value in values:
    bst_root = insert(bst_root, value)
pre_order_result = pre_order_traversal(bst_root)
post_order_result = post_order_traversal(bst_root)
print("Travessia (pré-ordem):", pre_order_result)
print("Travessia (pós-ordem):", post_order_result)