class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (f"Memory:{self.memory}GB",
                f"Hard Disk:{self.hdd}GB",
                f"Graphics Card:{self.gpu}")
        return "\n".join(info)


class ComputerBuilder:
    def __init__(self):
        self.coumputer = Computer("a243234")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
