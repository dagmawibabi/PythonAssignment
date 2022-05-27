def primePorcupine(start, end):
    s = start
    e = end
    i = 0
    for i in range(s, e):
        c = 0
        for j in range(1, e):
            if i % j == 0:
                c += 1
        if c == 2:
            if i % 10 == 9:
                print(i, " is a prime porcupine.")


primePorcupine(0, 140)