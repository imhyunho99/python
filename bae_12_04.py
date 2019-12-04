num = int(input())
num_list = input().split()
for i in range(num+1):
    num_list[i] = int(num_list[i])
q = int(input())
for i in range(q):
    s, e = map(int, input().split())
    s_list =[]
    e_list =[]
    all_list = []

    num = num_list[s:e+1]
    if s in s_list and e in e_list and s_list.index(s) == e_list.index(e):
        all = all_list[s_list.index(s)]
        print(all)
    else:
        if len(num) == 1:
            print(1)
        else:
            all = 0
            for j in range(len(num) // 2 + 1):
                if num[j] == num[len(num) - j - 1]:
                    all += 1
                else:
                    break
            if all == len(num) // 2:
                all = 1
                all_list.append(all)
                print(all)
            else:
                all_list.append(all)
                all = 0
                print(all)
            s_list.append(s)
            e_list.append(e)