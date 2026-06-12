class TrieNode:
   def __init__(self):
       self.children = {}  # Dictionary to store child nodes.
       self.isEnd = False  # Flag to represent end of a word.

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            if s in node.children:
                node = node.children[s]
            else: return False
        
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else: return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna