from datetime import date

from nldate import parse


class Tests:
    def test_one(self):
        assert parse("December 10, 2015") == date(2015, 12, 10)

    def test_two(self):
        assert parse("in 3 days", date(2015, 12, 10)) == date(2015, 12, 13)

    def test_three(self):
        assert parse("in a week", date(2015, 12, 10)) == date(2015, 12, 17)

    def test_four(self):
        assert parse("in a year", date(2015, 12, 10)) == date(2016, 12, 10)

    def test_five(self):
        assert parse("in 3 months", date(2015, 12, 10)) == date(2016, 3, 10)

    def test_six(self):
        assert parse("last year", date(2015, 12, 10)) == date(2014, 12, 10)

    def test_seven(self):
        assert parse("next Monday", date(2025, 6, 16)) == date(2025, 6, 23)

    def test_eight(self):
        assert parse("today") == date.today()

    def test_nine(self):
        assert parse("tomorrow", date(2015, 12, 10)) == date(2015, 12, 11)

    def test_ten(self):
        assert parse("12/10/2015") == date(2015, 12, 10)
