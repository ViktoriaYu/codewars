'''
You get a list of non-zero integers A, its length is always greater than one.
Your task is to find such non-zero integers W that the weighted sum
A0⋅W0+A1⋅W1+..+An⋅Wn
is equal to 0.
'''

def weigh_the_list(a):
    w = []
    if len(a) % 2 == 0:
        for i in range(0, len(a), 2):
            w.append(a[i+1])
            w.append(-a[i])
    else:
        w.append(a[1]*a[2])
        w.append(-2*a[0]*a[2])
        w.append(a[0]*a[1])
        if len(a) > 3:
            for i in range(3, len(a), 2):
                w.append(a[i+1])
                w.append(-a[i])
    return w
