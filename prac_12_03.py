num = int(input())#7
num_list = input().split()#1 2 1 3 1 2 1
for i in range(num):
    num_list[i] = int(num_list[i])
q = int(input())
s_list = []
e_list = []
all_list = []
for i in range(q):#4
    what = 0
    s, e = map(int, input().split())#1 3
    num = num_list[s-1:e] #3
    if s in s_list and e in e_list and s_list.index(s) == e_list.index(e):
        print(all_list[s_list.index(s)])
    else:
        if len(num) == 1:
            what = 1
            print(1)
        else:
            all = 0
            for j in range(len(num) // 2):#2
                if num[j] == num[len(num) - j -1]:
                    all += 1
                else:
                    break
            if all == len(num) // 2:
                what = 1
                print(1)
            else:
                what = 0
                print(0)
            s_list.append(s)
            e_list.append(e)
            all_list.append(what)
