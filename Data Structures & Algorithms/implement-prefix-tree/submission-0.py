class Node:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
        curr_node.is_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        
        return curr_node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return True
        

        