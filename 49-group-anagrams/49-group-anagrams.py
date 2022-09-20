class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # distinguish using dictionary
        str_dic = {}
        
        for e in strs:
            temp = sorted(e)
            ordered_e = ''.join(temp)
            
        # below setence(line14) causes unhashable type 'list'!
        # Because sorted() make each letter to an element of list. That's whay I use join method to make string again.
            
            if ordered_e not in str_dic:
                str_dic[ordered_e] = [e]
            else:
                str_dic[ordered_e].append(e)
                
        # take only values from dictionary
        answer = []
        
        for k, v in str_dic.items():
            answer.append(v)

        return answer