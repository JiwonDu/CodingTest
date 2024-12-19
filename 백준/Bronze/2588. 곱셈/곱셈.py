A = int(input())
B = int(input())

B_1 = B % 10
B_2 = (B // 10) % 10
B_3 = B // 100

print(A * B_1)
print(A * B_2)
print(A * B_3)

print(A * B)
