import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove asterisk and blank using regular expression
        filtered_str = re.sub(r"[^a-zA-Z0-9]", '', s)
        
        # change lower case to upper case
        result = filtered_str.lower()

        # reverse a result with list method
        result_list = list(result)
        result_list.reverse()
        result_reversed = ''.join(result_list)
        
        return result == result_reversed