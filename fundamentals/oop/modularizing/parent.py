local_val = "magical unicorns"


def square(x):
    return x*x


class User:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return "Hello World"
my_user = User('Patrick')
print(square(5))
print(my_user.say_hello())


if __name__ == "__main__":
    print("the file is being executed directly")
    print(square(5))
else: 
    print("The file is being executed because it is imported by another file. The file is called: ", __name__) 