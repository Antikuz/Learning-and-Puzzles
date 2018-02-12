def max(items, key=lambda x: x[1]):
    current = item[0]
    for item in items:
        if key(item) > key(current):
            print("По ключу ")
            current = item
    return current
    
a = [[1, 0], [2, 1], [9, 0]]