def odd_nums(n):
    result = []
    for num in range(1, n+1, 2):
        result.append(num)
    return iter(result)

odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
