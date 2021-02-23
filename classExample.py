class Human:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def ageFinder(self):
        if self.age<18:
            print(self.name +" is underage")
        else:
            print(self.name + " is not underage")


suman=Human("suman",18)
kriti=Human("krity",17)

suman.ageFinder()
kriti.ageFinder()