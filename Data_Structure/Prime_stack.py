from Linked_List import LinkedList


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        return self.list.insert_at_end(data)

    def peek(self):
        return self.list.get_last()

    def pop(self):
        return self.list.remove_last()

    def display(self):
        return self.list.display()


def prime_list(a, b):
    list_ = []
    for i in range(a, b):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 2:
            continue
        if count < 2:
            list_.append(i)
    return list_


def anagram(a, b):
    list_ = []
    prime_ = prime_list(a, b)

    for i in range(len(prime_)):
        for j in range(i+1, len(prime_)):
            if sorted(str(prime_[i])) == sorted(str(prime_[j])):
                list_.append(prime_[i])
                list_.append(prime_[j])
    return list_


if __name__ == "__main__":
    container = Stack()
    a = 1
    b = 1000
    out_list = anagram(a, b)
    rev_list = []
    for i in out_list:
        container.push(i)
    for i in out_list:
        rev_list.append(container.peek())
        container.pop()
    print(rev_list)
