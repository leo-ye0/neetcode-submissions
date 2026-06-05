class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes (e.g., 'l' -> Node)
        self.children = {}
        # Flag to mark if this node represents the end of a full word
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # If the path doesn't exist, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True only if it's marked as a complete word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True if we successfully traversed the prefix
        # We don't care if it's an end_of_word or not
        return True
        
        