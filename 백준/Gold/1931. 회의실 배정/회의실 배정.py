meeting = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    meeting.append([a,b])

meeting.sort(key=lambda x : (x[1], x[0]))
ans = 1; last = meeting[0][1]
for i in range(1, len(meeting)):
    start_time, last_time = meeting[i]
    if last <= start_time:
        last = last_time
        ans += 1
print(ans)
            