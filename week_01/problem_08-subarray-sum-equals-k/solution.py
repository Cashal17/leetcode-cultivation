class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ans = 0
        # for i in range(len(nums)):
        #     currSum = 0
        #     for j in range(i, len(nums)):
        #         currSum += nums[j]
        #         if currSum == k:
        #             ans += 1
        # return ans

        # prefix sum: [i+1] = [i-1] + arr[i+1]
        # sum from i to j = sum from start to j - sum from start to i 
        ans = 0
        prefixSum = 0 
        counter = {0: 1}    # the prefixSum value -> # of unique subarrays equal to that sum
        for num in nums: 
            prefixSum += num
            # if current sum and number needed to equal k already in hashmap ->
            # add # of subarrays since each duplicate will be unique and valid subarray
            ans += counter.get(prefixSum - k, 0)    
            counter[prefixSum] = counter.get(prefixSum, 0) + 1      # recording entry in hashmap
        return ans 
        
