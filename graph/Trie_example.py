def add(word):
    cur = {}
    for ch in word:
        if ch not in cur:
            cur[ch] = {}
            print('this is ch {} and cur[ch]'.format(ch, cur[ch]))
        cur = cur[ch]
        # print(cur)

a = add('woshihaorennnn')
print(a)