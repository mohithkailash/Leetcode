class Codec:
    def __init__(self):
        self.encoder = {}
        self.decoder = {}
        self.base = "http://tinyurl.com/"
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encoder:
            shortUrl = self.base + str(len(self.encoder))
            self.encoder[longUrl] = shortUrl
            self.decoder[shortUrl] = longUrl
            
        return self.encoder[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoder[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))