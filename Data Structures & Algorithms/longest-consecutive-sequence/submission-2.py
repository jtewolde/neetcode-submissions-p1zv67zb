class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initial approach by using hash set
        
        # Convert the given nums array to a set
        # Create a longest_seq variable to keep track of the current longest sequenece
        # Iterate through each number in the set

        # For the current num, if there is no num - 1 in the set, make the current seq variable = 1
        # Otherwise, Loop through/keep seeing if there is a consective sequence of numbers for the current num
        
        # Example: Current num = 2 --> Loop to see if there is 3 in the set --> current_seq += 1 --> Same for 4,5..., until the consective streak breaks
        # Then, Make longest_seq the maximum value between the longest sequence record and the current sequence of the number
        # return the longest_seq variable

        numSet = set(nums)
        longest_seq = 0 

        # Iterate through the set
        for num in numSet:
            # If there is no num - 1 in the set, reset/start current_seq to one
            if (num - 1) not in numSet:
                current_seq = 1
            
                # Loop through the consective numbers for the current num until the consective streak breaks
                while(num + current_seq) in numSet:
                    current_seq += 1

                longest_seq = max(longest_seq, current_seq)

        return longest_seq
