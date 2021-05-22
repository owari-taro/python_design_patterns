class Hoge:
    def __init__(self,name,**kwargs):
        self.name=name
        print(kwargs)
        for key in kwargs:
            print(key,kwargs[key])
            setattr(self,key,kwargs[key])

if __name__=="__main__":
    keywords=("test","hoge","sad")
    hoge=Hoge("hogehoge",keywords=keywords)
    print(hoge)