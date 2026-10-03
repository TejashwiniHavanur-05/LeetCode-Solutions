class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        answer=[]
        greatest=max(candies)
        for i in range(len(candies)):
           result=candies[i]+extraCandies>= greatest
           answer.append(result)
        return answer
        
