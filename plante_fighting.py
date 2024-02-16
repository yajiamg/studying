from random import randint as ra
import pygame
from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # 显然这个题应该要用动态规划的思想去解决
        # construct a vector
        dp=list(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            for j in range(k):
                dp[i]=max()

