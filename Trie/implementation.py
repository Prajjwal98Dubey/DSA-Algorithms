class TrieNode:
    def __init__(self):
        self.children =[None] * 26     # we can also take hashmap 
        self.endOfWord = False
# 0->a 1->b ..... 25->z
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertion(self,word):
        curr = self.root
        for c in word:
            index =  ord(c) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord=True
    def search(self,word):
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index]==None:
                return False
            curr= curr.children[index]
        return curr.endOfWord
    def checkPrefix(self,prefix):
        curr = self.root
        for c in prefix:
            index =  ord(c) - ord("a")
            if curr.children[index]==None:
                return False
            curr = curr.children[index]
        return True
    def deleteWord(self,word):
        # check if the word is present or not.
        if not self.search(word):
            return "Word is not present in trie."
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            node = curr.children[index]
            curr.children[index]=None
            curr =  node
        curr.endOfWord = False
trie1 = Trie()
trie1.insertion("apple")
trie1.insertion("appleee")
# print("Before deletion ", trie1.search("appleee"))
trie1.insertion("batman")
trie1.deleteWord("appleee")
# print("After deletion ", trie1.search("appleee"))
print(trie1.deleteWord("superman"))
# print(trie1.deleteWord("batman"))
print(trie1.search("batman"))

# print(trie1.search("appleee"))
# print(trie1.checkPrefix("bat"))
