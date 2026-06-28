class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        index1 = len(s) - 1
        index2 = len(t) - 1
        while (index1 >= 0 or index2 >= 0):
            i1 = self.get_next_valid_char_index(s, index1)
            i2 = self.get_next_valid_char_index(t, index2)
            if i1 < 0 and i2 < 0: 
                return True
            if i1 < 0 or i2 < 0:  
                return False
            if s[i1] != t[i2]: 
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True


    def get_next_valid_char_index(self, str, index):
        backspace_count = 0
        while (index >= 0):
            if str[index] == '#':  
                backspace_count += 1
            elif backspace_count > 0:  
                backspace_count -= 1
            else:
                break

            index -= 1  

        return index

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna