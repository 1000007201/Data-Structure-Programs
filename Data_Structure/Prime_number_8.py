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


if __name__ == "__main__":
    array = []
    a = 1
    b = 100
    while b < 1000:
        out_list = prime_list(a, b)
        array.append(out_list)
        a += 100
        b += 100

    print(array)
