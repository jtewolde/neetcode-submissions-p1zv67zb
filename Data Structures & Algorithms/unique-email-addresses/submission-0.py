class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Approach: Use iteration/built-in functions to find unique email addresses
        # Create a hashset called unique, that will store unique addressed
        # Then, iterate through all emails in the emails array
        # Use built-in functions ike split and remove to normalize each email
        # First, use split function to split the local part and domain part from email
        # Then, only using the local part, use split to locate '+' in local if any and take only first part
        # Use replace function to get rid of all periods in local and replace with empty string
        # Finally, combine new local and domain together for complete email address and add to unique set

         # Create a hashset called unique, that will store unique addresses
        unique = set()

        # Then, iterate through all emails in the emails array
        # Use built-in functions ike split and remove to normalize each email
        for e in emails:
            # First, use split function to split the local part and domain part from email
            local, domain = e.split('@')
            # Then, only using the local part, use split to locate '+' in local if any and take only first part
            local = local.split('+')[0]
            # Use remove function to get rid of all periods in local since periods don't have any effect
            local = local.replace('.', "")
            # Finally, combine new local and domain together for complete email address and add to unique set
            normalizedEmail = local + domain
            unique.add(normalizedEmail)

        return len(unique)
