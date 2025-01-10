names = ("Alice", "Bob", "Charlie")

x = list(map(lambda name : "Hello, " + name + " Hello!" , names))

print(" ".join(x).center(200))

# Second option:
# def doSomething(name):
#    return "Hello, "+name+" Hello!"
# x = list(map(doSomething, names))

# print(" ".join(x).center(200))

