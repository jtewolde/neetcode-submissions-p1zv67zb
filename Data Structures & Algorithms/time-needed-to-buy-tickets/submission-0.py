class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Approach: Use iteration to simulate how tickets are bought across fans in queue order
        # Track how many seconds/turns it takes to for person at index k to get all of their tickets
        # There are two solutions for iteration, one for simulating the entire process
        # Another iteration solution that I will do is directly calculating the answer 
        # By considering how each person in tickets array will buy before person k finishes
        # Example: [2,3,2,5,9], k = 3 where tickets[k] = 5
        # Indx 0 -> 2 < 5 -> ans += 2, Indx 1 -> 3 < 5 -> ans += 3, Indx 2 -> 2 < 5

        # Initialize ans variable that will count the number of seconds/turns it takes for person k to finish
        ans = 0

        # Iterate through each person in tickets array
        for indx in range(len(tickets)):
            # Case 1: If current indx in tickets is before position k, 
            # Increment ans with the min between tickets[indx] and tickets[k]
            if indx <= k:
                ans += min(tickets[indx], tickets[k])

            # Case 2: If current indx in tikets is after position k,
            # Increment ans wit hthe min beween tickets[i] and tickets[k] - 1
            if indx > k:
                ans += min(tickets[indx], tickets[k] - 1)
        return ans
