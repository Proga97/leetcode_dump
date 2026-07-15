class Solution:
    def numTrees(self, n: int) -> int:
        numTrees = [1] * (n + 1)

        #0 nodes = 1 tree
        #1 node = 1 tree
        #          left, right
        #4 nodes = nodes[0] * nodes[3] +
        #          nodes[1] * nodes[2]  
        #          nodes[2] * nodes[1]  
        #          nodes[3] * nodes[0]  

        for nodes in range(2, n+1):
            total = 0
            for roots in range(1, nodes + 1):
                left = roots - 1
                right = nodes - roots
                total += (numTrees[left] * numTrees[right])
            numTrees[nodes] = total
        
        return numTrees[n]
                         

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna