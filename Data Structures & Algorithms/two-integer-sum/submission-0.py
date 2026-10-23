class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, num in enumerate(nums):
            complement = map.get(target - num)

            if complement != None:
                return [complement, index]
            else:
                map[num] = index
        
        return None