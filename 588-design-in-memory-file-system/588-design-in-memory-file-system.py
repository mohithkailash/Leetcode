class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    
    def find(self,path):#find and return node at path.
        curr=self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            curr=curr.children[word]
        return curr
    
    
    def ls(self, path: str) -> List[str]:
        cur=self.find(path)
        if cur.content:
            return [path.split('/')[-1]]
        return sorted(cur.children)
            

    def mkdir(self, path: str) -> None:
        self.find(path)
        # paths = path.split("/")
        # cur = self.root
        # for node in paths:
        #     if node not in cur.children:
        #         cur.children[node] = TrieNode()
        #     cur = cur.children[node]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.find(filePath)
        # paths = filePath.split("/")
        # cur = self.root
        # for node in paths:
        #     if node not in cur.children:
        #         cur.children[node] = TrieNode()
        #     cur = cur.children[node]
        cur.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.find(filePath)
        # paths = filePath.split("/")
        # cur  = self.root
        # for node in paths:
        #     cur = cur.children[node]
        return cur.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)