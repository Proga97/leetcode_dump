class TreeNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
    
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode()
            node = node.children[w]
        node.isEnd = True

    def dfs(self, node, j,word):
        for i in range(j,len(word)):
            w = word[i]
            # print(word,w,i,j)
            if w == ".":
                for child in node.children:
                    if self.dfs(node.children[child],i+1,word):
                        return True
                return False
            else:
                if w not in node.children:
                    return False
                node = node.children[w]
        return node.isEnd

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node,0,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna