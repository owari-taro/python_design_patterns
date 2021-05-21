from enum import Enum
from abc import ABCMeta,abstractmethod

State=Enum('State','new running sleeping restart zombie')
class Server(metaclass=ABCMeta):
  @abstractmethod
  def __init__(self):
    pass
  def __str__(self):
    return self.name
  
 @abstractmethod
def boot(self):
  pass
@abstractmethod
def kill(self,restart=True):
   pass
  
 class FileServer(Server):
    def __init__(self):
      slef.name="FileServer"
      self.state=State.new
     
    def boot(self):
      print(f"botting the {self}")
      self.state=State.running
     
   def kill(self,restart=True):
    print(f"killing {self}")
    self.state=State.restart if restart else State.zombie
  
  def create_file(self,user,name,permissions):
    print(f"trying to create thte file")
