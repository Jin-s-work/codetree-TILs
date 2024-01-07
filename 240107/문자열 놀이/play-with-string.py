s, q = map(str, input().split())

for i in range(int(q)):
    k, a, b = map(str, input().split())
    
    if k == '1':
        a, b = int(a), int(b)
        s_list = list(s)
        s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]
        s = ''.join(s_list)
        print(s)
    elif k == '2':
        s = s.replace(a, b)
        print(s)
        
    # if int(k) == 1:
    #     a = int(a)
    #     b = int(b)
    #     ans = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    #     print(ans)
    #     s = ans
    # elif int(k) == 2 and len(a) == 1:
    #     ans = ""
    #     ans = ''.join([b if char == a else char for char in s])

        # for st in s:
        #     if st == a:
        #         ans += b
        #     else:
        #         ans += st
        # print(ans)
        # s = ans