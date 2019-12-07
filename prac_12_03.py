k = int(input())
count = 0
for i in range(k):
    s = input()
    alpha_count = []
    alpha_set = []
    for j in range(len(s)):
        if s[j] not in alpha_set:
            alpha_set.append(s[j])

    for j in range(len(alpha_set)):
        alpha_count.append(0)
    for j in range(len(s)):
        if 0 not in alpha_count:
            break
        for l in range(len(alpha_set)):
            if alpha_set[l] == s[j]:
                alpha_count[l] += 1
    sum = 0
    for j in range(len(alpha_count)):
        sum += alpha_count[j]
    if sum == len(s):
        count += 1

print(count)