# Procedural Queue
# ================
def say_hello():
    print("Hello!")


def say_goodbye():
    print("goodbye!")
# Queue creation


def say_hello_again():
    print("Hello again!")


simpleQ = []

# Enqueue
simpleQ.append("Item 1")

# Peek
print(simpleQ[0])

# Dequeue
print(simpleQ.pop(0))
