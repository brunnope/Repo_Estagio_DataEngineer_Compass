a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
b = set(a)
b = b.intersection(b)
print(list(b))