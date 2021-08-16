src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for s in src[1:]:
    index = src.index(s)
    ind = index-1
    if s > src[ind]:
        result.append(s)
print(result)
