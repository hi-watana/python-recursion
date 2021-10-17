def fib(n):
    def _fib(k, a0, a1):
        while True:
            if k <= 1:
                return a1
            k, a0, a1 = k - 1, a1, a0 + a1
    return _fib(n, 1, 1)
