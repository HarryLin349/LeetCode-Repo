class MagicDictionary:
    '''
    naively: compare each string (n) with every entry in dictionary (d) and go char by char, checking diff (n) -> O(100*100*100)
    idea: track letter frequencies of words
    true if frequencies are the same except 2 letters .. still O(n) comparison and to build
    hashing? take a word and hash it
    for each word, replace with each of 26 letters and add to children

    '''
    from collections import defaultdict

    def __init__(self):
        self.children = set()
        self.letters = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                for letter in range(26):
                    cletter =chr(ord('a')+ letter)
                    if cletter == word[i]: continue
                    newword = word[:i] +  cletter + word[i+1:]
                    self.children.add(newword)

    def search(self, searchWord: str) -> bool:
        print("searching for", searchWord)
        # print(self.children)
        for i in range(len(searchWord)):
            if searchWord in self.children:
                print("Found", searchWord)
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)