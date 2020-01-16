
class Command():

    def __init__(self,receiver):
        self.receiver = receiver

    def execute(self):
        raise NotImplementedError

class ConcreteCommand(Command):

    def execute(self):
        self.receiver.action()

class Receiver():
    def action(self):
        print("receiver actiono")

class Invoker():
    def setCommand(self,command):
        self.command = command
    def executeCommand(self):
        self.command.execute()



if __name__ == '__main__':

    receiver = Receiver()
    cm = ConcreteCommand(receiver)
    ik = Invoker()
    ik.setCommand(cm)
    ik.executeCommand()