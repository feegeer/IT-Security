if __name__ == '__main__':
    key = ''.join([str(bin(int(x, base=16))[2:].zfill(8)) for x in '1F-DD-4F-41-7B-77-BA-0B'.split('-')])

    pc1_c = '57 49 41 33 25 17 9 ' \
            '1 58 50 42 34 26 18 ' \
            '10 2 59 51 43 35 27 ' \
            '19 11 3 60 52 44 36'.split(' ')

    pc1_d = '63 55 47 39 31 23 15 ' \
            '7 62 54 46 38 30 22 ' \
            '14 6 61 53 45 37 29 ' \
            '21 13 5 28 20 12 4'.split(' ')

    pc2 = '14 17 11 24 1 5 ' \
          '3 28 15 6 21 10 ' \
          '23 19 12 4 26 8 ' \
          '16 7 27 20 13 2 ' \
          '41 52 31 37 47 55 ' \
          '30 40 51 45 33 48 ' \
          '44 49 39 56 34 53 ' \
          '46 42 50 36 29 32'.split(' ')

    c = ''.join([key[int(x) - 1] for x in pc1_c])
    d = ''.join([key[int(x) - 1] for x in pc1_d])

    c1 = c[1:] + c[:1]
    d1 = d[1:] + d[:1]

    c1d1 = c1+d1

    k1_str = ''.join([c1d1[int(x) - 1] for x in pc2])
    k1 = [hex(int(k1_str[i:i + 4], 2))[2:] for i in range(0, len(k1_str), 4)]
    print(''.join(k1).upper())
