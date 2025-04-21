# BEATS 100% LETS GOOO
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        idea: construct a DAG of letters
        n1 -> n2 iff n1 < n2 
        cycle: invalid, return ""
        then do a topological ordering

        constructing the graph . .
        examine two neighbors, n1 and n2
        examine each i
        if unequal, break
        else, take the next and get a rule from them
        '''
        adjMap = {}
        vocabstr = "".join(words)
        vocab = set([char for char in vocabstr])
        print("vocab", vocab)
        for char in vocab:
            adjMap[char] = set()
        n = len(words)
        for i in range(n - 1):
            n1, n2 = words[i], words[i+1]
            print("comparing", n1, n2)
            ind = 0
            length = min(len(words[i]), len(words[i+1]))
            while ind < length and n1[ind] == n2[ind]:
                ind += 1
            # add a new rule based on the comparison
            if (ind < length):
                adjMap[n1[ind]].add(n2[ind])
            if (ind == length and len(n1) > len(n2)):
                print("impossible")
                return ""

        
        print("adjmap", adjMap)

        # now we traverse this adjMap to get a topological ordering
        completed = set()
        visited = set()
        hasCycle = False
        def dfs(node):
            nonlocal hasCycle
            if node in completed:
                return ""
            if node in visited:
                hasCycle = True
                print("found a cycle")
                return ""
            visited.add(node)
            descendants = ""
            for neighbor in adjMap[node]:
                descendants += dfs(neighbor)
                # explore neighbors
            visited.remove(node)
            completed.add(node)
            return node + descendants
        
        res = ""
        for letter in vocab:
            res = dfs(letter) + res
        return "" if hasCycle else res