t = int(input())

for i in range(1, t+1):
    n = int(input())

    activities = []

    for num in range(n):
        activity = list(map(int, input().split()))
        activity.append(num)

        activities.append(activity)

    # sort activities by start time
    activities.sort(key=lambda x: x[0])

    c_time = 0
    j_time = 0

    impossible = False

    for activity in activities:
        s = activity[0]
        e = activity[1]

        if s >= c_time:
            c_time = e
            activity.append('C')

        elif s >= j_time:
            j_time = e
            activity.append('J')

        else:
            impossible = True
            break

    if impossible:
        print("case #{}: IMPOSSIBLE".format(i))
    else:
        activities.sort(key=lambda x: x[2])
        print("case #{}: {}".format(i, "".join([x[3] for x in activities])))
