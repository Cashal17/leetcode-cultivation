class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # def twoSum(nums, target):
        #     dict = {}
        #     for i, num in enumerate(nums):
        #         addend = target - num
        #         if addend in dict:
        #             return [num, addend]
        #         dict[num] = i
        #     return []

        ans = []
        nums = sorted(nums)
        for i, num in enumerate(nums):  # each iter, fix ith value and check for other 2
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicates in sorted array
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # 3 possible cases
                # more than 0 -> move right to smaller val
                if sum > 0:
                    r -= 1
                # less than 0 -> move left to greater val
                elif sum < 0:
                    l += 1
                # equal zero -> valid triplet, skip duplicates
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return ans
        