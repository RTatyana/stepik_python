n, m = input().split()

s = []
for i in range(int(n)):
    s.append(str(input()))

palindrom = ''

for i in range(len(s)):
    if s[i] == s[i][::-1]:
        palindrom = s[i]
        s[i] = ''

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j][::-1]:
            palindrom = s[i] + palindrom + s[j]
            s[i] = ''
            s[j] = ''

print(len(palindrom))
print(palindrom)


