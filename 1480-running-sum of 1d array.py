class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result=0
        answer=[]
        for i in range(len(nums)):
            result=result+nums[i]
            answer.append(result)
        return answer
