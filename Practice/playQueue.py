from Queue import Queue

queue = Queue()
print(queue.has_space())
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(7)
queue.dequeue()
print(queue.peek())
print(queue.stringify())
