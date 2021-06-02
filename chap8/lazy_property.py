class LazyProperty:
    def __init__(self,method):
        self.method=method
        self.method_name=method.__name__
        
    def __get__(self,obj,cls):
        if not obj:
            return obj
        value=self.method(obj)
        setattr(obj,self.method_name,value)
        return value

class Test:
    def __init__(self):
        self.x=x
        self.y=y
        self._resource=None
    def 
    