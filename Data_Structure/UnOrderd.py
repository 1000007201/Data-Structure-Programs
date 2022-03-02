from Linked_List import LinkedList


if __name__ == "__main__":
    link = LinkedList()
    with open("sample.txt", 'r+') as file:
        data_file = file.read()
        file.truncate(0)
    list_file = data_file.split(" ")
    link.insert_values(list_file)
    data = "hello"
    present = link.is_present(data)
    if present:
        link.remove(data)
    else:
        link.insert_at_end(data)
    string_ = link.to_string()
    with open("sample.txt", 'w') as file:
        file = open("sample.txt", 'w')
        file.write(string_)