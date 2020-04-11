t = int(input())

for i in range(1, t + 1):
    s = list(input())

    new_s = list(s)

    cur_depth = 0
    it = -1

    while True:
        it += 1
        if it == len(new_s):
            break

        if new_s[it] in ('(', ')'):
            continue

        if int(new_s[it]) > cur_depth:
            diff = int(new_s[it]) - cur_depth
            cur_depth = int(new_s[it])
            new_s = new_s[:it] + ['('] * diff + new_s[it:]

        elif int(new_s[it]) < cur_depth:
            diff = cur_depth - int(new_s[it])
            cur_depth = int(new_s[it])
            new_s = new_s[:it] + [')'] * diff + new_s[it:]

        if it == len(new_s)-1:
            new_s.extend([')'] * cur_depth)
            break

    print("Case #{}: {}".format(i, "".join(new_s)))
