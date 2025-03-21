class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # idea: bfs over a graph constructed over words?
        # dp? backtracking? 

        # easy part: bfsing a graph of words
        # hard part: constructing that graph
        # for each word, checking all combos is o(nm) (n words, O(m) comparison)
        # total time O(n^2m) ... too slow?
        
        # could also try 26 comboes for each m letters..
        # 26 * m * n -> O(nm)
        # other ideas ..?
        # hard part is checking valid moves seems O(n) unless there's a smarter way

        wordSet = set(wordList)
        wordList.append(beginWord)
        wordMap = { word:[] for word in wordList}
        m = len(wordList[0])

        for word in wordList:
            # consider every 1 letter permutation
            for letterPos in range(m):
                for char in range(ord('a'), ord('z') + 1):
                    newWord = word[:letterPos] + chr(char) + word[letterPos + 1:]
                    # print("checking", newWord)
                    if newWord in wordSet and newWord != word:
                        # we have a valid change
                        wordMap[word].append(newWord)
        
        print(wordMap)

        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            cur, count = queue.pop(0)
            if cur == endWord:
                return count
            visited.add(cur)
            for nxt in wordMap[cur]:
                if nxt not in visited:
                    queue.append((nxt, count + 1))
        return 0

            