hour, minute = map(int, input().split())
total_minute = 0
total_minute += hour * 60 + minute - 30
if total_minute >= 1440:
    total_minute -= 1440
hour = total_minute // 60
minute = total_minute % 60
print(hour, minute)
