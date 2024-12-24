h, m = map(int, input().split())

def Alam(x, y):
    if y < 45:
        y += 60
        x -= 1
        if x < 0:
            x = 23

    m_new = y - 45
    return (x, m_new)

print(*Alam(h, m))
