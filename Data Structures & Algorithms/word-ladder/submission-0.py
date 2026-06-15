class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for char_code in range(97, 123): # 'a' to 'z'
                    char = chr(char_code)
                    if char == word[i]: continue
                    
                    next_word = word[:i] + char + word[i+1:]
                    
                    if next_word in wordSet:
                        wordSet.remove(next_word) # Acts as "visited"
                        queue.append((next_word, length + 1))
                        
        return 0