t = int(input())

for i in range(1, t + 1):
    n = int(input())

    matrix = []

    trace = 0
    r = 0
    c = 0

    for j in range(n):
        row = list(map(int, input().split()))

        row_set = set(row)
        if len(row_set) != n:
            r += 1

        matrix.append(row)
        trace += row[j]

    matrix_transpose = [*zip(*matrix)]

    for row in matrix_transpose:
        row_set = set(row)
        if len(row_set) != n:
            c += 1

    print("Case #{}: {} {} {}".format(i, trace, r, c)) #op
