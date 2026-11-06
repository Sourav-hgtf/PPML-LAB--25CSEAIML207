def even_len(n):
    s = []

    for i in n:
        if i % 2 == 0:
            s.append(i)

    return s

x = input("Enter the list elements: ")
n = [int(i) for i in x.split(",")]

s = even_len(n)

print("List containing even values:", s)