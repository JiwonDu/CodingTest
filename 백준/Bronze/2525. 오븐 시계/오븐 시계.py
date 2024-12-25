Hour, Min = map(int, input().split())
Time = int(input())

def Finish(x, y, z):
    total_minutes = (x * 60) + y + z
    h = total_minutes // 60
    m = total_minutes % 60
    if h > 23:
        h -= 24
    return h, m

end_hour, end_minute = Finish(Hour, Min, Time)
print(end_hour, end_minute)
