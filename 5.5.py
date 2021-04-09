src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

seen = set()
unique_value = []
for number in src:
    if (number in seen) and (number in unique_value):
        unique_value.remove(number)
    else:
        unique_value.append(number)
    seen.add(number)
print(unique_value)