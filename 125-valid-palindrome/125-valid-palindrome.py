import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove asterisk and blank using regular expression
        filtered_str = re.sub(r"[^a-zA-Z0-9]", '', s)
        
        # change lower case to upper case
        result = filtered_str.lower()

        # reverse a result str
        result_reversed = result[::-1]
        
        return result == result_reversed