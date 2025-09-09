from devprocess import multiply_numbers 

class TestMultiplyNumbers:
    def test_multiply_positive_numbers(MultiplyNumbers):
        assert multiply_numbers(5, 5) == 25

    def test_multiply_positive_numbers(MultiplyNumbers):
        assert multiply_numbers(7, 7) == 49