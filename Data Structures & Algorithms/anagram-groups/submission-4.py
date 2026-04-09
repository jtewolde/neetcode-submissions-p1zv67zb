class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # PseudoCode for problem:
       # Create a default dict that keeps track of the different anagramas created
       # Iterate through every string in list
       # Sort the current string and append it to the defaultDict
       # Put the different keys/values into seperate sublists
       
        result_dict = defaultdict(list);

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

