class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # idea here: heap 
        # maxheap will sort (BST) by highest to lowest
        # O(1) access for highest frequency 
        # O(logn) (nlogn for each)

        # naively: count each occurence of words in a dict
        # then store tuples of (count, word) with a custom sort function that sorts by count, then word

        # alternatively, count each occurence of words in a dict
        # then place each word in a heap

        wordCount = { word: 0 for word in words}
        for word in words:
            wordCount[word] += 1
        print (wordCount)

        sortedWords = []
        for word, count in wordCount.items():
            sortedWords.append((count, word))

        sortedWords.sort(key=lambda x: (-x[0], x[1]))
        
        res = []
        for i in range(k):
            res.append(sortedWords[i][1])
        return res