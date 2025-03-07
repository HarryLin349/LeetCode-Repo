class WordDictionary:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def addWord(self, word: str) -> None:
        cur_trie = self
        for i in range(len(word)):
            cur_char = word[i]
            if cur_char not in cur_trie.children:
                cur_trie.children[cur_char] = WordDictionary()
            cur_trie = cur_trie.children[cur_char]
        cur_trie.is_end = True


    def search(self, word: str) -> bool:

        # idea: for each letter in str
        # if it matches a child? progress or true if end
        # if its "."? search all children or true if end
        # else false

        cur_trie = self

        for i in range(len(word)):
            cur_char = word[i]
            if (cur_char == "."):
                # DFS on the children
                for key, val in cur_trie.children.items():
                    if val.search(word[i+1:]):
                        return True
                return False
            elif cur_char in cur_trie.children:
                cur_trie = cur_trie.children[cur_char]
            else:
                return False            
            if i == len(word) - 1:
                return cur_trie.is_end
        return cur_trie.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)