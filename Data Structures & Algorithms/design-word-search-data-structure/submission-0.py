class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    # If it's a dot, try every possible child branch
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # Normal character logic
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.is_end

        return dfs(0, self.root)
        
