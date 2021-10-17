def fact(n):
    def _fact(k, a):
        while True:
            if k <= 0:
                return a
            a = k * a
            k = k - 1
    return _fact(n, 1)
