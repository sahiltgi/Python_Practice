# MAXIMUM DEPTH OF BINARY TREE

def maxDepth(self, root) -> int:
    if (root == None):
        return 0
    if (root.left == None) and (root.right == None):
        return 1
    else:
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if (l > r):
            return l + 1
        else:
            return r + 1


if __name__ == "__main__":
    root = list(map(int, input().split()))
    print(maxDepth(root))
