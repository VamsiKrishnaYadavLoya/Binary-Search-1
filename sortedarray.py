# Time Complexity: O(log N)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# Your code here along with comments explaining your approach
#Since it is given array is sorted, from the mid value either left or right part of array is sorted 
# If target == mid, return mid
# Finding which part of the array is sorted. And proceed if left half sorted and element is in left half or vise versa

class Solution:
    def search(self, nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
