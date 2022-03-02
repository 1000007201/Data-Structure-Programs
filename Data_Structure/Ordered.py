from Linked_List import LinkedList


def string_to_list(number_string):
    _list = number_string.split()
    list_ = list(map(int, _list))
    return list_


if __name__ == "__main__":
    link = LinkedList()
    with open("sample2.txt", 'r+') as file:
        number_string = file.read()
        file.truncate(0)

    number_list = string_to_list(number_string)
    number_list.sort()

    link.insert_values(number_list)
    # link.display()

    user_number = int(input("Enter any number:"))

    present = link.is_present(user_number)
    if present:
        link.remove(user_number)
    else:
        link.add_num_to_sorted(user_number)
    # link.display()

    string_ = link.to_string()
    with open("sample2.txt", 'w') as file:
        file.write(string_)




