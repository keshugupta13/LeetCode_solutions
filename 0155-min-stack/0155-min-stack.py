class MinStack(object):

    def __init__(self):
        self.s=[]
        self.temp=[]
        self.minEle=None
        

    def push(self, val):
        if len(self.temp)==0 or val<=self.temp[-1]:
            self.temp.append(val)
        self.s.append(val)
        
        

    def pop(self):
        if not self.s:
            return -1
        if self.s[-1]==self.temp[-1]:
            self.temp.pop(-1)
        return self.s.pop(-1)
        

    def top(self):
        return self.s[-1]

        

    def getMin(self):
        if not self.temp:
            return -1
        return self.temp[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()