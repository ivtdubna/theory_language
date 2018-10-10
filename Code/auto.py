class auto():
    abc = []
    condition = []
    final_condition = []
    init_condition = None
    delta = []
    current_condition = None

    def __init__(self, set_abc, set_condition, set_final_condition, q0):
        self.abc = set_abc
        self.condition = set_condition
        self.final_condition = set_final_condition
        self.init_condition = q0
        self.current_condition = q0

    def add_delta(self, lst):
        if (lst[0] in self.condition and lst[1] in self.abc and lst[2] in self.condition):
            self.delta.append(lst)

    def work(self, input_str):
        for i in input_str:
            for d in delta:
                if self.current_condition == d[0] and i == d[1]:
                    self.current_condition = d[2]
        if self.current_condition in self.final_condition:
            return True
        else:
            return False

        

    
    
