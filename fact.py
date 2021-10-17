def fact(n):
    def _fact(k, a):
        while True:
            if k <= 0:
                return a
            k, a = k - 1, k * a
    return _fact(n, 1)
