class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Approach: Use a sliding window techinque to create a window of given size k
        # Take the sum of elements outside of the window and track 
    
        # Finally, return ans as final max answer

        # Initially, take the sum of the last k cards at the end of the cards array
        # Then, create left and right pointers where left starts at 0 and right starts at before last k cards
        left, right = 0, len(cardPoints) - k
        curTotal = sum(cardPoints[right:])
        ans = curTotal

        # Create a while loop while right is less than total length of cardPoints 
        while right < len(cardPoints):
            # Update the total by adding the difference between val at left and right pointers
            # Then, update the ans variable with maximum between ans and total
            curTotal += cardPoints[left] - cardPoints[right]
            ans = max(ans, curTotal)

            # Move left and right pointers forward in the array
            left += 1
            right += 1
        return ans

