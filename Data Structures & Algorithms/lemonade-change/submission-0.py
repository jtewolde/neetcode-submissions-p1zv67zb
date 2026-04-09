class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Approach: Use Greedy algorthrim to keep track of how much change you have after customer purchase
        # Create two variables, five and ten, for keeping inventory of all $5 and $10 dollars collected from purchase
        # Iterate through the bills array
        # For each purchase, update inventory of five and ten dollars purchases based on current element
        # If current element is a 5, increment five counter by one and vice versa for ten
        # If encountering 20 dollar purchases in array, use Greedy to determine which bills to use from inventory to give change
        # 

        # Initialize five and ten counters to keep track of inventory of bills
        five, ten = 0, 0

        # Iterate through bills array and update inventory of bills accordingly based on element
        for i in range(len(bills)):
            # Case 1: Customer uses $5 bill, no change required, update five counter
            if bills[i] == 5:
                five += 1
            # Case 2: Customer uses $10 bill, change of $5 needed, increment ten counter and decrement five
            elif bills[i] == 10:
                ten += 1
                five -= 1
            # Case 3: Customer uses $20 bill, change of $ 15 required, use Greedy to determine what bills are used for change
            else:
                # If we have ten dollars in inventory, use one ten and one five for change
                if ten > 0:
                    ten -= 1
                    five -=1 
                # Otherwise, just use 3 five bills for change of $15
                else:
                    five -= 3

            # Check if there are still five dollar bills in inventory for change
            # IF there is none, return False as no change can be given back
            if five < 0:
                return False

        return True
            
            
