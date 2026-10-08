import math
class Embedding:
    def __init__(self,values):
        self.values=[]
        for v in values: self.values.append(float(v))
    def print(self): print("Embedding("+str(self.values)+")")
    def equals(self,other): return self.values==other.values
    def get(self,i): return self.values[i]
    def size(self): return len(self.values)
    def iterate(self):
        for i in range(len(self.values)): yield self.values[i]
    def getMin(self):
        m=self.values[0]
        for i in range(len(self.values)):
            if self.values[i]<m: m=self.values[i]
        return m
    def getMax(self):
        m=self.values[0]
        for i in range(len(self.values)):
            if self.values[i]>m: m=self.values[i]
        return m
    def getMean(self):
        s=0
        for i in range(len(self.values)): s=s+self.values[i]
        return s/len(self.values)
    def add(self,other):
        if len(self.values)!=len(other.values): raise ValueError("size mismatch")
        result=[]
        for i in range(len(self.values)): result.append(self.values[i]+other.values[i])
        return Embedding(result)
    def divide(self,divisor):
        result=[]
        for i in range(len(self.values)): result.append(self.values[i]/divisor)
        return Embedding(result)
    @staticmethod
    def average(embeddings):
        total=embeddings[0]
        for i in range(1,len(embeddings)): total=total.add(embeddings[i])
        return total.divide(len(embeddings))
    def dot(self,other):
        d=0
        for i in range(len(self.values)): d=d+self.values[i]*other.values[i]
        return d
    def norm(self): return math.sqrt(self.dot(self))
    def cosine(self,other): return self.dot(other)/(self.norm()*other.norm())
