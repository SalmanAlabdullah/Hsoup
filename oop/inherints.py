

class employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def info(self):
        print(self.first + '_' + self.last)



ahmed = employee('ahmed','khald')

ahmed.info()

class programmer(employee):
    def __init__(self,first,last,proj):
        employee.__init__(self,first,last)
        self.proj = proj

    def a_proj(self,a_proj):
        self.proj = [a_proj]

    def g_proj(self):
        print(self.proj)


salman = programmer('salman','abdulaziz',['ios','sam'])

salman.a_proj(['sa','ss'])
salman.g_proj()

a = []
a.append('sa')
print(a)
a.append('a')
print(a)
