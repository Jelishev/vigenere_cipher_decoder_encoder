class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.k = list(key)
        self.a = list(alphabet)
        #print(self.a, self.k)
    def encode(self, text):
        while len(self.k) < len(list(text)):
            self.k +=self.k
        a = list(text)
        t = []
        for x in a:
            if x in self.a:
                t.append(self.a.index(x))
            else:
                t.append(0)
        p = [self.a.index(x) for x in self.k]
        final = ""
        for i in range(0,len(t)):
            if a[i] in self.a:
                final += self.a[(t[i]+p[i])%(len(self.a))]
            else:
                final += a[i]
        print(final)
        return final
    
    def decode(self, text):
        while len(self.k) < len(list(text)):
            self.k +=self.k
        a = list(text)
        t = []
        for x in a:
            if x in self.a:
                t.append(self.a.index(x))
            else:
                t.append(0)
        p = [self.a.index(x) for x in self.k]
        final = ""
        for i in range(0,len(t)):
            if a[i] in self.a:
                final += self.a[abs((t[i]-p[i])%(len(self.a)))]
            else:
                final += a[i]
        print(final)
        return final
