import datetime as date

from nldate import parse


class Tests:
    def test_the_tests(self):
        assert date.datetime(2025, 10, 10) == date.datetime(2025, 10, 10)

    def test_one(self):
        assert parse("October 12, 2025") == date(2025, 10, 12)

    # def test_two(self):
    #     assert parse("Last week", date(2024, 2, 16)) == date(2024, 2, 9)

    # def test_three(self):
    #     assert parse("Tomorrow", date(2024, 2, 16)) == date(2024, 2, 17)

    # def test_four(self):
    #     assert parse("a week from today", date(2024, 2, 16)) == date(2024, 2, 23)

    # def test_five(self):
    #     assert parse("Ten days from tomorrow", date(2024, 2, 10)) == date(2024, 2, 21)

    # def test_six(self):
    #     assert parse("December 12 2025") == date(2025, 12, 12)

    # def test_seven(self):
    #     assert parse("12/10/2025") == date(2025, 12, 10)

    # def test_eight(self):
    #     assert parse("5/10/93") == date(1993, 5, 10)

    # def test_nine(self):
    #     assert parse("five days ago", date(2024, 5, 10)) == date(2024, 5, 5)

    # def test_ten(self):
    #     assert parse("Four years from now", date(2024, 5, 5)) == date(2029, 5, 5)
