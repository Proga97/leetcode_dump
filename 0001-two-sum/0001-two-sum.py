class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                # Initialize a HashMap to store the number and its index
        hashtable = {}

        # Iterate through the array
        for x in range(len(nums)):
            # Calculate the complement (remaining value to reach the target)
            remain = target - nums[x]
            
            # Check if the complement is already in the HashMap
            if remain in hashtable:
                # If found, return the indices of the complement and the current number
                return [hashtable[remain], x]
            
            # If not found, store the current number and its index in the HashMap
            hashtable[nums[x]] = x
        