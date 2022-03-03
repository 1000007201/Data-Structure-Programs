from Linked_List import LinkedList
from Prime_stack import anagram


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        return self.list.insert_at_beg(data)

    def dequeue(self):
        return self.list.remove_last()

    def display(self):
        return self.list.display()


if __name__ == "__main__":
    queue = Queue()
    a = 1
    b = 1000
    out_list = anagram(a, b)
    for i in out_list:
        queue.enqueue(i)
    queue.display()