class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Brute force approach: Iterate through each detail in the detals array
        # Skip the first 11 characters in detail, get chars from index 12-13 for age of passanger
        # See if age of passenger > 60, increase count variable

        count = 0

        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                count += 1
                print(count)

        return count


