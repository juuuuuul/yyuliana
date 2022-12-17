import itertools 
class leonardo: 
    class _leonardo_iter: 
        def __init__(self): 
            self.candy = 1   
            self.newyear = 1  
            self.cake = 0   
            self.tree = 0 
 
        def __next__(self): 
            self.tree += 1 
            if self.tree == 1:
                return 1
            if self.tree == 0:
                return 1
            else:
                self.cake = self.candy + self.newyear 
                self.candy = self.newyear
                self.newyear = self.cake 
                return self.newyear
    def __iter__(self): 
        return leonardo._leonardo_iter() 
f = leonardo() 
for i in itertools.islice(f, 31): 
    print(i)
