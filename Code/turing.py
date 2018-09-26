class turing():

    abc = None
    condition = None
    line = []
    rules = None
    action = ["r","l","q"]
    head = []

    def __init__(self, n):
        for i in range(n):
            self.line.append(" ")
        self.head = [0,"s0"]
        self.abc = []
        self.condition = ["s0","q"]
        self.rules = []
        
    def add_abc(self,a):
        self.abc.append(a)

    def add_condition(self, c):
        self.condition.append(c)

    def add_rules(self, r):
        if ((r[0] in self.abc) and (r[1] in self.condition) and (r[2] in self.abc) and (r[3] in self.condition) and (r[4] in self.action)):
            self.rules.append(r)
        else:
            print("Error")

    def add_text_line(self, txt):
        j = 1
        for i in txt:
            if (i in self.abc):
                self.line[j] = i
                j+=1
            else:
                print("Error")
                break;
    def print_line(self):
        s="".join(self.line)
        print(s)

    def print_head(self, n):
        s=""
        for i in range(len(self.line)):
            if i==n:
                s+="^"
            else:
                s+=" "
        print(s)
        
    def work(self):
        while self.head[1]!="q":
            for r in self.rules:
                if self.line[self.head[0]]==r[0] and self.head[1]==r[1]:
                    self.print_line()
                    self.print_head(self.head[0])
                    self.line[self.head[0]] = r[2]
                    self.head[1] = r[3]
                    if r[4]=="r":
                        self.head[0]+=1
                    elif r[4]=="l":
                        self.head[0]-=1
                    else:
                        break



T = turing(100)

#T.add_abc("a")
#T.add_abc("b")
#T.add_condition("S1")
#T.add_condition("S2")
#T.add_condition("S3")
#T.add_condition("S4")
#T.add_condition("S5")

#T.add_rules([" ", "S0", " ", "S0", "R"]) #1
#T.add_rules(["b", "S0", "b", "Q", "Q"]) #2
#T.add_rules(["a", "S0", " ", "S1", "R"]) #3
#T.add_rules(["a", "S1", "a", "S1", "R"]) #4
#T.add_rules([" ", "S1", " ", "Q", "Q"]) #5
#T.add_rules(["b", "S1", "b", "S2", "R"]) #6
#T.add_rules(["b", "S2", "b", "S2", "R"]) #7
#T.add_rules(["a", "S2", "a", "Q", "Q"]) #8
#T.add_rules([" ", "S2", " ", "S3", "L"]) #9
#T.add_rules(["b", "S3", " ", "S4", "L"]) #10
#T.add_rules(["b", "S4", "b", "S4", "L"]) #11
#T.add_rules(["a", "S4", "a", "S5", "L"]) #12
#T.add_rules([" ", "S4", " ", "Q", "Q"]) #13
#T.add_rules(["a", "S5", "a", "S5", "L"]) #14
#T.add_rules(["b", "S5", "b", "Q", "Q"]) #15
#T.add_rules([" ", "S5", " ", "S0", "R"]) #16

#T.add_text_line("aabbb")


T.add_abc("(")
T.add_abc(")")
T.add_abc("*")
T.add_abc(" ")

T.add_condition("s1")
T.add_condition("s2")
T.add_condition("s3")
T.add_condition("s4")
T.add_condition("s5")

T.add_rules([" ", "s0", " ", "s0", "r"])
T.add_rules([")", "s0", ")", "q", "q"])
T.add_rules(["(", "s0", "(", "s1", "l"])
    
T.add_rules([" ", "s1", "*", "s2", "r"])

T.add_rules(["(", "s2", "(", "s2", "r"])
T.add_rules([")", "s2", ")", "s2", "r"])
T.add_rules([" ", "s2", "*", "s3", "l"])

T.add_rules([" ", "s3", " ", "s3", "l"])
T.add_rules(["*", "s3", "*", "q", "q"])
T.add_rules([")", "s3", ")", "s3", "l"])
T.add_rules(["(", "s3", " ", "s4", "r"])

T.add_rules([")", "s4", " ", "s5", "r"])
T.add_rules([" ", "s4", " ", "s4", "r"])
T.add_rules(["*", "s4", "*", "q", "q"])

T.add_rules([" ", "s5", " ", "s5", "r"])
T.add_rules(["(", "s5", "(", "s5", "r"])
T.add_rules([")", "s5", ")", "s5", "r"])
T.add_rules(["*", "s5", "*", "s3", "l"])

T.add_text_line("((((((((()))))))))(()()()))")
