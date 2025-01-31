s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

positions = [s.find(char) for char in alphabet]

print(*positions)
