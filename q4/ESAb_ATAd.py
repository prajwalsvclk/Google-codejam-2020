from enum import Enum


class State(Enum):
    SURE = 1
    UNSURE = 2


def compute_possibilities(old_bits):
    mask = int('1' * head_num_of_known_bits + '0' * (b - head_num_of_known_bits - tail_num_of_known_bits) + '1' * tail_num_of_known_bits, 2)

    complement = ((1 << b) - old_bits - 1) & mask
    reverse = int('{:0{width}b}'.format(old_bits, width=b)[::-1], 2)
    complement_reverse = int('{:0{width}b}'.format(complement, width=b)[::-1], 2)

    return {
        (old_bits, head_num_of_known_bits, tail_num_of_known_bits),
        (complement, head_num_of_known_bits, tail_num_of_known_bits),
        (reverse, tail_num_of_known_bits, head_num_of_known_bits),
        (complement_reverse, tail_num_of_known_bits, head_num_of_known_bits)}


def eliminate_possibilities(sure, bit_pos, possible):
    still_possible = set()
    for poss in possible:
        binary = '{:0{width}b}'.format(poss[0], width=b)
        if binary[bit_pos - 1] == str(sure):
            still_possible.add(poss)
    return still_possible


def unsure_bit_to_query(possible):
    possibilities = list(possible)
    # find rightmost different bit in first two possibilities
    position = b - (possibilities[0][0] ^ possibilities[1][0]).bit_length() + 1

    if position > b:
        # same bit array but with different head/tail known bits
        # compare with another possibility if one exists
        # it is impossible for a second collision based on the mathematical operations
        if len(possibilities) > 2:
            position = b - (possibilities[0][0] ^ possibilities[2][0]).bit_length() + 1
        else:
            return -1
    return position


t, b = list(map(int, input().split()))


for _ in range(t):
    head_num_of_known_bits = 0
    tail_num_of_known_bits = 0
    queries_made = 0
    state = State.SURE

    sure_bits = 0
    poss_bits = []

    while True:

        if (head_num_of_known_bits + tail_num_of_known_bits) == b:
            # we found the entire bit array!
            print('{:0{width}b}'.format(sure_bits, width=b), flush=True)
            result = input()

            if result == 'Y':
                break
            else:
                # maybe we should have a recover mechanism if the judge thinks we're wrong
                # but we're greedy and we're never wrong
                exit()

        # bit array will permute on next query, exception for startup -> it doesn't matter
        if (queries_made + 1) % 10 == 1 and queries_made != 0:
            poss_bits = compute_possibilities(sure_bits)

            if len(poss_bits) == 1:
                # only possibility, we are sure of the value
                soln = list(poss_bits)[0]
                sure_bits = soln[0]
                head_num_of_known_bits = soln[1]
                tail_num_of_known_bits = soln[2]
                state = State.SURE
            else:
                state = State.UNSURE

        if state == State.SURE:

            if (head_num_of_known_bits - tail_num_of_known_bits) <= 0:
                query_pos = head_num_of_known_bits + 1
                head_num_of_known_bits += 1
            else:
                query_pos = b - tail_num_of_known_bits
                tail_num_of_known_bits += 1

            queries_made += 1

            print(query_pos, flush=True)

            sure_bits |= int(input()) << (b - query_pos)

        elif state == State.UNSURE:

            # find rightmost different bit in first two possibilities
            query_pos = unsure_bit_to_query(poss_bits)

            # we know the bit string but unsure about head/tail known bits
            # change state to SURE and we pretend we just didn't know the bit in the middle
            if query_pos == -1:
                soln = list(poss_bits)[0]
                sure_bits = soln[0]
                head_num_of_known_bits = min(soln[1], soln[2])
                tail_num_of_known_bits = min(soln[1], soln[2])
                state = State.SURE
                continue

            queries_made += 1
            print(query_pos, flush=True)

            sure_bit = int(input())

            poss_bits = eliminate_possibilities(sure_bit, query_pos, poss_bits)

            if len(poss_bits) == 1:
                # only possibility, we are sure of the value
                soln = list(poss_bits)[0]
                sure_bits = soln[0]
                head_num_of_known_bits = soln[1]
                tail_num_of_known_bits = soln[2]
                state = State.SURE
            else:
                state = State.UNSURE
