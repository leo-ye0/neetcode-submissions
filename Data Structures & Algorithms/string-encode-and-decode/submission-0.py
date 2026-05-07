class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the delimiter to get the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # Extract the string based on the length
            # Start index: j + 1 (right after the '#')
            # End index: j + 1 + length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
            
        return res