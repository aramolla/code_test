str = input()
answer=""
for s in str:
    if s.isupper():
        answer += s.lower()
    elif s.islower():
        answer += s.upper()
print(answer)
