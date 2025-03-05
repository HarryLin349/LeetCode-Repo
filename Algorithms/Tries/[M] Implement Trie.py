class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word: str) -> None:
        cur_node = self
        for index in range(len(word)):
            cur_char = word[index]
            if (cur_char in cur_node.children):
                cur_node = cur_node.children[cur_char]
            else:
                new_node = Trie()
                cur_node.children[cur_char] = new_node
                cur_node = new_node
            if (index == len(word) - 1):
                cur_node.is_end = True

    def search(self, word: str) -> bool:
        cur_node = self
        for index in range(len(word)):
            cur_char = word[index]
            if cur_char not in cur_node.children:
                return False
            cur_node = cur_node.children[cur_char]
            if (index == len(word) - 1):
                return cur_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self
        for index in range(len(prefix)):
            cur_char = prefix[index]
            if cur_char not in cur_node.children:
                return False
            cur_node = cur_node.children[cur_char]
            if (index == len(prefix) - 1):
                return True
        

# idea: each Node has an array of children (TrieNode)
# a value
# and a bool "isEnd:"


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)