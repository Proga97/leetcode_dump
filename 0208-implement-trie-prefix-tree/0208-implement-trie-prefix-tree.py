class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.isEnd = False  # Flag to represent end of a word.

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            ch = self.charToIndex(ch)
            print(ch)
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            ch = self.charToIndex(ch)
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.isEnd      
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            ch = self.charToIndex(ch)
            if ch not in root.children:
                return False
            root = root.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)