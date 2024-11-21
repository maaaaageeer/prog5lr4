class FibonacchiLst():
    def __init__(self,instance) -> None:
        self.instance = instance
        self.idx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]
            except IndexError:
                raise StopIteration
            
            # Обрабатываем отрицательный и нулевой случай (из)
            if res < 0:
                self.idx += 1
            elif res == 0:
                self.idx +=1
                return res
            else:
                fib = lambda x: True if (5*(x**2)-4) ** (1/2)%1 == 0 or (5*(x**2)+4) ** (1/2) %1 == 0 else False
                
                if fib(res):
                    self.idx +=1
                    return res
                self.idx +=1
            
