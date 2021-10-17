def fib(n):
    def _fib(k, cont):
        if k <= 1:
            return cont(1)
        return _fib(k - 1, lambda x: _fib(k - 2, lambda y: cont(x + y)))
    return _fib(n, lambda x: x)
