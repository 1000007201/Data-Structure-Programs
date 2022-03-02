from Stack_ import Stack

stack = Stack()

open_list = ['[', '{', '(']
close_list = [']', '}', ')']


def is_balance(string):
    for i in string:
        if i in open_list:
            stack.push(i)
        if i in close_list:
            position = close_list.index(i)
            if stack.size() > 0 and open_list[position] == stack.peek():
                stack.pop()
            else:
                print("Unbalanced")
                return
    if stack.size() == 0:
        print("Balanced")
        return
    else:
        print("Unbalanced")


input_string = "(({[]}))"
is_balance(input_string)



