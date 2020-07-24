#(7) Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for x in d:
            if d[x] == 1:
                answer.append(x)
        return answer