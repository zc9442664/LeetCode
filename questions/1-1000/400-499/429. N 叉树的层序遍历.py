# File Name:  429. N 叉树的层序遍历
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        result = []
        while queue:
            result.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return result


