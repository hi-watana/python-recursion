def fib(n):
    def _fib(k, a0, a1):
        if k <= 1:
            return a1
        return _fib(k - 1, a1, a0 + a1)
    return _fib(n, 1, 1)
