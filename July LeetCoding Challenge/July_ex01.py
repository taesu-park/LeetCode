#(1) Top K Frequent Elements

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        result = []
        heapq.heapify(result)
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return heapq.nlargest(k, d, key=d.get)