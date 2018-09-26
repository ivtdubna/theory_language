import random

class gramm:
    __rules=[]

    def add_rule(self, S):
        self.__rules.append(S)

    def look(self):
        return self.__rules

    def deduct(self, L, n):
        while (n!=0):
            r=random.randint(0, len(self.__rules)-1)
            st=self.__rules[r]
            if L.find(st[0])!=-1:
                L=L.replace(st[0],st[1])
                print(L)
            n-=1
        return L

a=gramm()
a.add_rule(["S","(S)"])
a.add_rule(["S","SS"])
a.add_rule(["S",""])

