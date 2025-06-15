from collections import deque

friends = deque(('rolf', 'charlie', 'jen', 'anna'))
print(friends)

friends.append("ron")
friends.appendleft("sample")
print(friends)

friends.pop()
friends.popleft()
print(friends)

