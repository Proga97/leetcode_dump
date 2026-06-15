class TrieNode:
    def  __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isEnd = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i+1)
            node = trie.root
            for j in range(i,len(s)):
                if s[j] not in node.children:
                    # print("break",i,j,s[j])
                    break
                node = node.children[s[j]]
                if node.isEnd:
                    res = min(res,dfs(j+1))
            dp[i] = res
            return res
        
        return dfs(0)



        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna