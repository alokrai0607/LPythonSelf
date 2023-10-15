list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

box = []
minlen = min(len(list1), len(list2))

for i in range(minlen):
    box.append(list1[i] + list2[i])

box.extend(list1[minlen:])
box.extend(list2[minlen:])

print(box)
