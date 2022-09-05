
class FixedQueue:
    def __init__(self, size: int):
        self.size = size
        self.storage = [None] * self.size
        self.queueSize = 0

        self.frontPointer = 0
        self.rearPointer = 0

    def enqueue(self, item):
        if self.queueSize == self.size:
            raise MaxQueueSize
        else:
            self.storage[self.rearPointer] = item

            self.rearPointer += 1

            if self.rearPointer == self.size:
                self.rearPointer = 0

            self.queueSize += 1

    def dequeue(self):
        if self.queueSize == 0:
            raise EmptyQueue
        else:
            dequeuedItem = self.storage[self.frontPointer]
            self.frontPointer += 1
            self.queueSize -= 1
            return dequeuedItem

    def enqueue_prio(self, item):
        if self.queueSize == self.size:
            raise MaxQueueSize
        else:
            self.storage[self.frontPointer - 1] = item
            self.frontPointer -= 1
            self.queueSize += 1

    def peek(self):
        return self.storage[self.frontPointer]

    def peekAll(self):
        displayDict = {
            "Front Pointer: ": self.frontPointer,
            "Rear Pointer: ": self.rearPointer,
            "Current Storage: ": self.storage,
            "Current Size: ": self.queueSize,
            "Next dequeue: ": self.storage[self.frontPointer]
        }

        for key, value in displayDict.items():
            print(key, value)


class QueueError(Exception):
    """Exceptions for queues"""


class MaxQueueSize(QueueError):
    def __init__(self):
        super().__init__("Queue at max size")


class EmptyQueue(QueueError):
    def __init__(self):
        super().__init__("Queue is empty")
