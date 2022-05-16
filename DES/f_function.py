
# list comprehension heaven
if __name__ == '__main__':
    r = ''.join([str(bin(int(x, base=16))[2:].zfill(8)) for x in '37-CC-AF-11'.split('-')])
    k = ''.join([str(bin(int(x, base=16))[2:].zfill(8)) for x in '14-0E-1F-33-BB-0A'.split('-')])
    k = [k[i:i + 6] for i in range(0, len(k), 6)]

    e_selection = '32 1 2 3 4 5 4 5 6 7 8 9 8 9 10 11 12 13 ' \
                  '12 13 14 15 16 17 16 17 18 19 20 21 20 21 22 ' \
                  '23 24 25 24 25 26 27 28 29 28 29 30 31 32 1'.split(' ')

    lines = [line[:-1].split(' ') for line in open('S_tables', 'r').readlines()]
    s_tables = [(lines[i:i + 5])[:-1] for i in range(0, len(lines), 5)]

    p = '16 7 20 21 29 12 28 17 1 15 23 26 5 18 31 10 2 8 24 14 32 27 3 9 19 13 30 6 22 11 4 25'.split(' ')

    e_r_str = ''.join([r[int(x) - 1] for x in e_selection])
    e_r = [e_r_str[i:i + 6] for i in range(0, len(e_r_str), 6)]

    xored = [str(bin(int(e_r[i], 2) ^ int(k[i], 2))[2:].zfill(6)) for i in range(0, len(e_r))]

    j_values = [int(x[1:5], 2) for x in xored]
    i_values = [int(x[0] + x[5], 2) for x in xored]

    chosen_values = ''.join(
        [str(bin(int(s_tables[k][i_values[k]][j_values[k]]))[2:].zfill(4)) for k in range(0, len(i_values))])

    encoded_str = ''.join([chosen_values[int(x) - 1] for x in p])
    encoded = [hex(int(encoded_str[i:i + 4], 2)) for i in range(0, len(encoded_str), 4)]
    print(''.join(encoded).upper())