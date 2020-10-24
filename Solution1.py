# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     Solution1
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/24 12:47 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/24:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'


class Solution:
    def twoSum(self, nums, target):
        for x in range(0, len(nums)):
            rest = target - nums[x]
            if nums.__contains__(rest) and nums.index(rest) != x:
                return [x, nums.index(rest)]


if __name__ == "__main__":
    nums = [3, 3]
    # nums = [3, 2, 4]  test case 2
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"result is {result}")

