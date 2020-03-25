# BINARY TREE INORDER TRAVERSAL

def inorderTraversal(self, root):
    if not root:
        return []
    result = []
    result.extend(self.inorderTraversal(root.left))
    result.append(root.val)
    result.extend(self.inorderTraversal(root.right))
    return result


if __name__ == "__main__":
    root = list(map(int, input().split()))
    print(inorderTraversal(root))