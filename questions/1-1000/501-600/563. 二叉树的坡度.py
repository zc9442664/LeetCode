# File Name:  563. 二叉树的坡度
# date:       2021/4/12
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        nodes, index, n = [root], 1, len(nums)
        for node in nodes:
            if node != None:
                if index == n:
                    return root
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.left)
                index += 1
                if index == n:
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.right)
                index += 1

    def findTilt(self, root: TreeNode) -> int:
        self.result = 0

        def heaper(node):
            if not node: return 0  # 叶子节点子树和默认为0
            left_sum = heaper(node.left)
            right_sum = heaper(node.right)
            self.result += abs(left_sum - right_sum)  # 左子树和右子树之差的绝对值为坡度
            return left_sum + right_sum + node.val  # 返回子树所有值和

        heaper(root)
        return self.result


nodes = [21, 7, 14, 1, 1, 2, 2, 3, 3]
test = Solution()
root = test.buildBinaryTree(nodes)
print(test.findTilt(root))
