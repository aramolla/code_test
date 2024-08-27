N = int(input()) # 입력할 키의 수

for _ in range(N):
    key = int(input()) # 키
    for i in range(2, 1000001):
        if key % i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")

