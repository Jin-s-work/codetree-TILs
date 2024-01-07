s, q = map(str, input().split())

for i in range(int(q)):
    k, a, b = map(str, input().split())
    
    if int(k) == 1:
        a = int(a)
        b = int(b)
        print(s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])
        s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    elif int(k) == 2:
        ans = ""
        for st in s:
            if st == a:
                ans += b
            else:
                ans += st
        print(ans)
        s = ans