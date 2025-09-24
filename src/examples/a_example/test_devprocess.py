from devprocess import add_num as add_numbers   


class TestAddNumbers:
    def test_add_positive_numbers(self):
        assert add_numbers(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add_numbers(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add_numbers(-2, 3) == 1  