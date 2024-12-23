
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result=0
        l,r=0,len(nums)-1
        nums.sort()
        while(l<r):
            if(nums[l]+nums[r]>k):
                r-=1
            elif(nums[l]+nums[r]<k):
                l+=1
            else:
                result+=1
                l+=1
                r-=1
        return result