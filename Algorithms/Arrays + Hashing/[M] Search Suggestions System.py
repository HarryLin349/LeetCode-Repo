class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''
        idea:
        probably use a trie? 
        maintain a trie of all products, insert each product in

        then for each char, search trie for that prefix, returning the top 3 lexographical hits
        using ... backtracking ? how do we get the minimum 3

        alt: sorted list of products
        then each prefix level just contains a subset of that list ..?
        whittle down the entire thing, and return the first 3
        probably really slow but we can try it

        maintain a current list (only ever shrinking)
        while i < len(searchterm)
            curquery += searchterm[i]
            on each pass, add to newlist whichever words start with curword
            set curlist to newlist
        '''
        curlist = sorted(products)
        curquery = ""
        i = 0
        res = []
        for i in range(len(searchWord)):
            newlist = []
            curquery += searchWord[i]
            k = len(curquery) 
            for word in curlist:
                if len(word) >= k and word[:k] == curquery:
                    newlist.append(word)
            res.append(newlist[:3])
            curlist = newlist
        return res