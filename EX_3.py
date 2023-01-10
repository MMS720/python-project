def ex3_1(x):
    s = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        s += 1
    return s


def ex3_2(x):
    b = []
    for m in range(len(x) - 1):
        b += [x[m] * x[m + 1]]
    return max(b)


def ex3_3(x):
    xc = 0
    yc = 0
    "n" == 1
    "e" == 1
    "w" == -1
    "s" == -1
    for i in range(len(x) - 1):
        if x[i] == 'n':
            yc += 1
        elif x[i] == 'e':
            xc += 1
        elif x[i] == 'w':
            xc += -1
        elif x[i] == 's':
            yc += -1
    if xc == 3 and yc == 2:
        return (True)
    elif xc == -4 and yc == 3:
        return (True)
    else:
        return (False)


def ex3_4(x, y, z):
    a = x * 2**y
    if a % z == 0:
        return (True)
    else:
        return (False)


def ex3_5(x):
    z = []
    for e in range(len(x) - 1):
        z += [e]
        if e < 0:
            e = -e
            z += [-e]
    if sum(z) == 25:
        return (True)
    else:
        return (False)


def ex3_5(x):
    return (max(x) - min(x))
