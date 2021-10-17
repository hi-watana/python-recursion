def fib(n):
    memo = [0] * (n + 1)
    def _fib(k):
        if k <= 1:
            return 1
        if memo[k] > 0:
            return memo[k]
        memo[k] = _fib(k - 1) + _fib(k - 2)
        return memo[k]
    return _fib(n)
