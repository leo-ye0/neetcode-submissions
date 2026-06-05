class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
            
        rows, cols = len(board), len(board[0])
        res = []
        # 2. Backtracking Function
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None # Avoid duplicate findings

            # Mark visited
            board[r][c] = "#"
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            
            # Backtrack (restore character)
            board[r][c] = char

        # 3. Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return res