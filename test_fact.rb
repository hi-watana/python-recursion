require 'test/unit'
require './recursive_functions'

class TestFact < Test::Unit::TestCase
  def test_fact_n_is_0
    assert_equal(1, fact(0))
  end

  def test_fact_n_is_6
    assert_equal(720, fact(6))
  end
end
