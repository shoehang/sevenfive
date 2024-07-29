'''
Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # guaranteed 2+ elements in nums, store first element in dictionary
        # store actual value for lookup, problem wants indicies returned
        d = { nums[0] : 0 }

        print(d)

        # start at second element
        for i in range(1, len(nums)):

            # return when difference of target and current number is in dict
            if (target - nums[i]) in d:
                return [d[target - nums[i]], i]
            
            # store new number
            d[nums[i]] = i