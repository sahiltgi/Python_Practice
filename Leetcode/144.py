# BINARY TREE PREORDER TRAVERSAL

def preorderTraversal(self, root):
    if not root:
        return []
    result = []
    result.append(root.val)
    result.extend(self.preorderTraversal(root.left))
    result.extend(self.preorderTraversal(root.right))
    return result


if __name__ == "__main__":
    root = list(map(int, input().split()))
    preorderTraversal(root)
