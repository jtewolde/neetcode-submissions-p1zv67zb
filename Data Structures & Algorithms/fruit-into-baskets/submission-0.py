class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Approach: Use a sliding window that will have 2 fruit types max inside,
        # Fruit types are unique numbers inside of fruit array: [1, 2, 2, 3, 3] has 3 fruit types due 
        # When encountering a third fruit type, shrink the window from the left until the two types remain
        # Goal is to find a maximum continous subarray in fruits that only contain 2 distinct fruit types

        # Initialize a count by using defaultDict hashmap to get freq of each number in fruits array
        # Also, create left pointer of sliding window 
        count = defaultdict(int)
        left = 0

        # Use the right pointer to iterate through fruits array for sliding window
        for right in range(len(fruits)):
            # Add the fruit type at right to the count hashmap
            count[fruits[right]] += 1

            # If there are more than two fruits/keys in counter,
            # then decrement count of fruit at left pointer of sliding window
            if len(count) > 2:
                count[fruits[left]] -= 1

                # If the count of the fruit type at left are 0, pop it from the count
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                # Increment left pointer by one
                left += 1

        # Get the difference between the length of ruits array and value of left pointer
        # This will return the maximum window size
        return len(fruits) - left