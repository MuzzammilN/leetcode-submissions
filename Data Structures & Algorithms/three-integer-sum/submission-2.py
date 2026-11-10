class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0

        nums.sort()
        out = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                tg = nums[i] + nums[left] + nums[right]

                if tg > 0:
                    right -= 1

                if tg < 0: 
                    left += 1

                if tg == 0:
                    if [nums[i],nums[left],nums[right]] in out:
                        left += 1
                        right -= 1
                        continue

                    out.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

        return out