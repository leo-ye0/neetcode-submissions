class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize adjacency list and in-degree map for all unique characters
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Check the prefix edge case trap (e.g., "abcd" before "abc")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            # Find the first mismatching character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    parent, child = w1[j], w2[j]
                    if child not in adj[parent]:
                        adj[parent].add(child)
                        in_degree[child] += 1
                    break # Only the first mismatching character gives us order info
                    
        # Step 3: Collect all nodes with 0 incoming dependencies
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        # Step 4: Run Kahn's Algorithm (BFS)
        while queue:
            curr = queue.popleft()
            result.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 5: If result contains all unique characters, we found a valid order
        if len(result) == len(in_degree):
            return "".join(result)
            
        return ""