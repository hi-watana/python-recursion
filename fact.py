def fact(n):
    def _fact(k, cont):
        if k <= 0:
            return cont(1)
        return _fact(k - 1, lambda x: cont(x * k))
    return _fact(n, lambda x: x)
