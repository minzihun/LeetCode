import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # change upper case to lower case
        paragraph = paragraph.lower()
        
        # remove special words
        paragraph = re.sub(r'[^\w\s]'," ", paragraph)
        
        # prevent exceptional case
        banned.sort()
        banned.reverse()
        
        # remove banned words
        for e in banned:
            paragraph = paragraph.replace(e, "")

        # make a list to split the sentence with space
        paragraph_list = paragraph.split()
        
        # put all elements to dictionary
        cnt_dic = {}
        
        for e in paragraph_list:
            if e not in cnt_dic:
                cnt_dic[e] = 1
            else:
                cnt_dic[e] += 1
        
        return max(cnt_dic, key=cnt_dic.get)