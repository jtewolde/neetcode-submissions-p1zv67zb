class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Approach for solving this problem is using Greedy
        # The trick for this problem is to find nums in triplets that can form the target
        # If any num in any triplets are greater than corresponding num in target, disregard it

        # Initialize a set, ans_nums, which will keep track of numbers that fit with target
        ans_nums = set()

        # Iterate through number in each triplet,
        # If any numbers in the triplets are greater than num in target, disregard and continue
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for index, val in enumerate(t):
                if val == target[index]:
                    ans_nums.add(index)

        return len(ans_nums) == 3

        