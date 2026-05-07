class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            # sorted('eat') -> ['a', 'e', 't'] 
            # "".join(...) -> "aet"
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        return list(anagram_map.values())