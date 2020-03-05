s=input()
a = len(s)
i = 0
count = 1    
while i <= (a/2):
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break

if count == 1:
    print('Yes')
else:
    print('No')