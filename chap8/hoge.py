class Klass:
    def __new__(cls, arg1, arg2):
        print(f"{cls=}")
        print("new:", arg1, arg2)
        tmp = object.__new__(cls)
        print(tmp.__dict__)
        # print(f"{tmp=}")
        return tmp

    def __init__(self, arg1, arg2):
        print("hogehoge")
        self.arg1 = arg1
        self.arg2 = arg2
        print(self.__dict__)


if __name__ == "__main__":
    a = Klass("te", "sf")
    print()
