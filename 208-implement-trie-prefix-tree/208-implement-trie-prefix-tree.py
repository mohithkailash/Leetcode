class Trie:

    def __init__(self):
        self.myset = set()

    def insert(self, word: str) -> None:
        self.myset.add(word)
        return

    def search(self, word: str) -> bool:
        if word in self.myset:
            return True

    def startsWith(self, prefix: str) -> bool:
        for i in self.myset:
            if prefix in i[0:len(prefix)]:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)