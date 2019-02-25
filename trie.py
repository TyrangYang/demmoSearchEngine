class TrieNode:
    def __init__(self):
        self.children = {}
        self.key = None
        self.value = None
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value=None): ## INSERT A WORD IN TRIE
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            currentNode.key = char
        currentNode.is_word = True
        currentNode.value = value

    def isWordExist(self,word): ## RETURN A WORD IF IN THE TRIE OR NOT
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        if currentNode.is_word:
            return True
        else:
            return False

    def searchValue(self, word): ## RETURN THE VALUE OF A WORD. IF THE WORD IS TOTALLY NOT IN TRIE, THIS RETURN NONE. IF THE WORD IS PART EXIST IN TRIE, THIS RETURN FLASE. SUCH AS: SOMETIME EXIST, SEARCH SOME WILL RETURN FLASE
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return None
            currentNode = currentNode.children[char]
        if currentNode.is_word:
            return currentNode.value
        else:
            return False

    def dfs(self, node): ## RETURN A LIST THAT CONTAIN ALL WORD IN TRIE WHICH ROOT IS GIVEN
        keylist = []
        if node.children:
            for char in node.children:
                partlist = self.dfs(node.children[char])
                if len(partlist) == 0:
                    keylist.append(char)
                elif node.children[char].is_word:
                    for word in partlist:
                        s = char + word
                        keylist.append(s)
                    keylist.append(char)
                else:
                    for word in partlist:
                        s = char + word
                        keylist.append(s)
        else:
            return []
        return keylist
 

    def getTrieNode(self, word): ## RETURN A NODE THAT GIVEN A WORD
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return None
            currentNode = currentNode.children[char]
        return currentNode
    
    def showAllKey(self): ## RETURN A LIST THAT CONTAIN ALL WORD IN TRIE
        return self.dfs(self.root)

# t = Trie()
# t.insert("bear", 12)
# # t.insert("bid", 21)
# # t.insert("buy", 12)
# t.insert("be", 33)
# t.insert("bea", 32)
# t.insert("bz", 32)
# # t.insert("sell")
# # t.insert("stop")
# print(t.searchValue("soeeee"), t.searchValue("bear"), t.searchValue("se"))
# print(t.root.children["b"].children["e"].is_word)
# print("dfs")
# result = t.dfs(t.root.children["b"])
# print(result)
# for word in result:
#     print(t.searchValue(word))