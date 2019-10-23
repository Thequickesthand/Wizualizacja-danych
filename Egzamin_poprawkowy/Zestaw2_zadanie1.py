def duplikaty (x):
    return list(set(x))

test = [34, 12, -3, 4, 5, 5, 12, -3]
print(test)
test = duplikaty(test)
print(test)