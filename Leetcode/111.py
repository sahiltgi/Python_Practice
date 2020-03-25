# MINIMUM DEPTH OF BINARY TREE

def minDepth(self, root) -> int:
    if (root == None):
        return 0
    if (root.left == None) and (root.right == None):
        return 1
    if (root.left == None):
        return 1 + self.minDepth(root.right)
    if (root.right == None):
        return 1 + self.minDepth(root.left)
    return min(self.minDepth(root.right), self.minDepth(root.left)) + 1


if __name__ == "__main__":
    root = list(map(int, input().split()))
    print(minDepth(root))
