class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or 
                board[r][c] not in node.children):
                return

            visit.add((r, c))

            # Add current tile and check if it's a word.
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)
            
            # DFS on neighboring positions.
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            
            visit.remove((r, c))
        
        # Call DFS on each tile (starting positions).
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

# GOAL
# ========
# Given a 2D grid and list of words, return all words
# present in the grid.

# OBSERVATIONS
# ========
# Each letter in the grid has four possible directions you can go in.

# IDEA
# ========
# Create trie based on words.
# Perform DFS on board. Build result.

