class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 2
        n = len(nums)
        if n < 3:
            return n
        for i in range(2, n):
            # If current number is not same element as two positions before count, keep it
            if nums[i] != nums[count-2]:
                nums[count] = nums[i]
                count += 1
            
        return count

        # freq = {}
        # count = 0
        # for i, num in enumerate(nums):
        #     # if consecutives are duplicate with freq > 2, skip count so first and last are kept
        #     if i < len(nums)-1 and nums[i] == nums[i+1]:
        #         freq[num] = freq.get(num, 1) + 1
        #         if freq[num] > 2:
        #             continue
        #     nums[count] = nums[i]
        #     count += 1
        # return count