students = set(range(1, 31))

submitted = set(int(input()) for _ in range(28))

missing = sorted(students - submitted)

print(missing[0])
print(missing[1])
