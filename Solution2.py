# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     Solution2
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/24 1:04 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/24:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        head2 = l2
        flag = False
        result_node = ListNode(-1, None)
        tmp_node = result_node
        while head1 is not None and head2 is not None:
            sum = head1.val + head2.val
            if flag:
                sum += 1
            flag = True if sum >= 10 else False
            print(f"sum%10: {sum % 10}  flag: {flag}")
            tmp_node.next = ListNode(sum % 10, None)
            tmp_node = tmp_node.next
            head1 = head1.next
            head2 = head2.next
            if head1 is None and head2 is not None:
                head1 = ListNode(0)
            if head2 is None and head1 is not None:
                head2 = ListNode(0)
            if head1 is None and head2 is None:
                if flag:
                    tmp_node.next = ListNode(1)
        return result_node.next


if __name__ == "__main__":
    node11 = ListNode(9)
    node10 = ListNode(9, node11)
    node9 = ListNode(9, node10)
    node8 = ListNode(9, node9)
    node7 = ListNode(9, node8)
    node6 = ListNode(9, node7)
    node5 = ListNode(9, node6)
    node4 = ListNode(9)
    node3 = ListNode(9, node4)
    node2 = ListNode(9, node3)
    node1 = ListNode(9, node2)

    solution = Solution()
    node = solution.addTwoNumbers(node1, node5)
    while node is not None:
        print(f"val: {node.val}, next: {node.next}")
        node = node.next
    print(f"result = {str(999 + 999)}")

