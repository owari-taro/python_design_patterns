MIN14="1.4GHz Mac mini"

class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.menory=4
            self.hdd=500
            self.gpu="intel hd graphics 5000"
        def __str__(self):
            info=(f"model:{MINI14}",f"memory:{self.memory}GB",f"hard disk:{self.hdd}",f"graphics card:{self.gpu}")
            return "\n".join(info)

    def build_computer(self,model):
        if model=="MINI14":
            return self.MacMini14()
        else:
            msg=f"I dont know how to build {model}"
            return msg
