class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0  
        right = len(numbers) - 1

        while left < right:
            t = numbers[left] + numbers[right]

            if t > target:
                right -= 1
                continue
            
            if t < target:
                left += 1
                continue

            if t == target:
                return [left + 1, right + 1]