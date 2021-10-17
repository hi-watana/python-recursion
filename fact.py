def fact(n):
    def _fact(k, a):
        if k <= 0:
            return a
        return _fact(k - 1, a * k)
    return _fact(n, 1)
