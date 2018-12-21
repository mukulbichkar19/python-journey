class Stacks(object):
    def __init__(self):
        this.self = self


def print_stack():
    print("Inside stack function")
    for s in stack:
        print(s)

stack = []; # declare a List

# push is similar to append in list i.e. adding at the end

stack.append(1)
stack.append(2)
stack.append(5)
stack.append(10)
stack.append(90)
stack.append(55)


# pop operation is similar to pop in list i.e. remove elements from end
stack.pop()
stack.pop()

print("stack size is: ")
print(len(stack))

print_stack()
