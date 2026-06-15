class TreeNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode()
            node = node.children[w]
        node.isEnd = True
    
    def dfs(self, node, prefix, curr_res):
        if len(curr_res) == 3:
            return
        
        if node.isEnd:
            curr_res.append(prefix)
        
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in node.children:
                self.dfs(node.children[ch],prefix+ch,curr_res)
    
    def search(self, prefix):
        node = self.root

        for n in prefix:
            if n not in node.children:
                return []
            node = node.children[n]
        
        curr_res = []
        self.dfs(node,prefix,curr_res)
        return curr_res
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        res = []
        node = trie.root
        prefix = ''
        for s in searchWord:
            prefix += s
            res.append(trie.search(prefix))
        
        return res





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna