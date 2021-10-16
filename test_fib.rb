require 'test/unit'
require './fib'

class TestFib < Test::Unit::TestCase
  def test_fib_n_is_0
    assert_equal(1, fib(0))
  end

  def test_fib_n_is_1
    assert_equal(1, fib(1))
  end

  def test_fib_n_is_4
    assert_equal(8, fib(4))
  end

  def test_fib_n_is_10
    assert_equal(89, fib(10))
  end
end
