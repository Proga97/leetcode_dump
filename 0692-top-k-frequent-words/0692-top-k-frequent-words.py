class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Flag to mark the end of a word

class Solution:
    def __init__(self):
        self.result = []
        self.k = 0
    def add_word(self, trie, word):
        root = trie
        for s in word:
            if s not in root.children:
                root.children[s] = TrieNode()
            root = root.children[s]
        root.is_end = True

    def get_words(self, root, word):
        if self.k == 0: return
        if root.is_end: 
            self.k -= 1
            self.result.append(word)
        for i in range(ord('a'), ord('z') + 1):
            s = chr(i)
            if s in root.children:
                self.get_words(root.children[s], word + s) 
        # for s, child in root.children.items():
        #     self.get_words(child, word + s) 

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ###  HEAP  #########
        # freq = Counter(words)
        # # print(freq)
        # heap = []
        # for string, count in freq.items():
        #     heappush(heap, (-count, string))
        
        # res = []
        # for _ in range(k):
        #     res.append(heappop(heap)[1])
        
        # return res

        #### TRIE + bucket sort ###
        n = len(words)
        freq = Counter(words)
        bucket = [None for _ in range(n+1)]
        self.k = k

        for string, count in freq.items():
            if bucket[count] is None:
                bucket[count] = TrieNode()
            self.add_word(bucket[count], string)
        
        for i in range(n, 0, -1):
            if bucket[i] is not None: self.get_words(bucket[i], "")

            if self.k == 0: return self.result
            
        
        return self.result




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna