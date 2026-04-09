class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Approach for solving this problem is to use Greedy techinque
        # Goal: See if the hand array can be dividable into the value of groupSize variable
        # Each group needs to increment by one each time, otherwise return false
        # Example: [2,3,4,5] & [5,6,7,8] == True

        # Check if the hand can even be divisible by the groupSize to create equal groups
        # If not, return False
        if len(hand) % groupSize != 0:
            return False

        # Use counter to get the frequencies of each number inside of hand array
        count = Counter(hand)

        # Sort the hands array to start with the minimum numbers first
        hands_sorted = hand.sort()
        
        # Process each number inside of the sorted hands array
        for num in sorted(hand):
            # If current number in hands hasn't been fully used yet, start a new group with it
            if count[num] > 0:
                # Create for loop to see if there are any number after num to add to group that follows conditions
                for next in range(num, num + groupSize):
                    # If the next number for group doesn't appear in hands array, return False as 
                    if count[next] == 0:
                        return False
                    # Decrement count for the next number in group
                    count[next] -= 1

        return True

