from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Approach: Sort the nums array using a custom comparator sorting helper function that will determine the order
        # The sorting function requires integers in nums to be converted into strings
        # Compare the sum between n1 + n2 and n2 + n1 to determine which concaternation of string is larger

        # Iterate through each integer in nums array and replace current integer with the string version
        for indx, num in enumerate(nums):
            nums[indx] = str(num)

        # Create a helper compare function that takes two num parameters 
        # And determine which concateration is bigger based on order. Return 1 or -1 based on sum
        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1
        
        # Sort the nums array based on the results of the helper compare function
        # Then, create ans variable that handles edge cases when there is a leading zero by converting to int then back to string
        nums = sorted(nums, key=cmp_to_key(compare))
        ans = str(int("".join(nums)))
        return ans
