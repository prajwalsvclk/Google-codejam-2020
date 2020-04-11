import numpy as np

t = int(input())


def fill_next_elem(m):
    m = np.copy(m)
    pos = np.unravel_index(np.argmin(m, axis=None), m.shape)

    if m[pos] != 0:
        if sum(np.diag(m)) == k:
            return m

    # diagonal
    if pos[0] == pos[1]:
        trace_so_far = sum(np.diag(m))

        if trace_so_far > k:
            return

        remaining_diags = len(m) - pos[0]

        trace_needed = k - trace_so_far
        trace_possible = remaining_diags * len(m)

        if trace_needed > trace_possible:
            return

    row_nums = set(m[pos[0], ...])
    col_nums = set(m[..., pos[1]])

    avail_nums = all_nums - row_nums - col_nums

    if len(avail_nums) == 0:
        return
    else:
        for num in avail_nums:
            m[pos] = num
            new_m = fill_next_elem(m)

            if new_m is not None:
                return new_m


for i in range(1, t+1):
    n, k = tuple(map(int, input().split()))

    matrix = np.zeros((n, n), dtype=int)

    all_nums = set(range(1, n+1))

    soln = fill_next_elem(matrix)

    if soln is not None:
        print("Case #{}: POSSIBLE".format(i))
        for row in soln:
            print(' '.join(map(str, row)))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))
