import unittest


from tags_equal import tags_equal


class TagsEqualTests(unittest.TestCase):

    """Tests for tags_equal."""

    def verifyEqual(self, tag1, tag2):
        if not tags_equal(tag1, tag2):
            raise AssertionError(f"{tag1!r} should equal {tag2!r}")

    def verifyNotEqual(self, tag1, tag2):
        if tags_equal(tag1, tag2):
            raise AssertionError(f"{tag1!r} should not equal {tag2!r}")

    def test_no_attributes(self):
        self.verifyEqual('<b>', '<b>')
        self.verifyNotEqual('<a>', '<b>')

    def test_different_case_of_tag_name(self):
        self.verifyEqual('<b>', '<B>')
        self.verifyNotEqual('<b>', '<A>')

    def test_with_matching_attributes(self):
        self.verifyEqual('<img width=400>', '<img width=400>')
        self.verifyEqual('<img width=400>', '<IMG width=400>')
        self.verifyNotEqual('<img width=400>', '<img width=200>')
        self.verifyNotEqual('<img width=400>', '<img height=400>')
        self.verifyNotEqual('<img width=400>', '<IMG height=400>')

    def test_with_multiple_matching_attributes(self):
        self.verifyEqual(
            '<img width=400 height=200>',
            '<img width=400 height=200>',
        )
        self.verifyNotEqual(
            '<img width=200 height=400>',
            '<img width=400 height=200>',
        )

    def test_different_order_attributes(self):
        self.verifyEqual(
            '<img height=200 width=400>',
            '<img width=400 height=200>',
        )
        self.verifyNotEqual(
            '<img height=400 width=200>',
            '<img width=400 height=200>',
        )

    def test_attributes_with_different_case(self):
        self.verifyEqual(
            '<input type=hidden>',
            '<input TYPE=hidden>',
        )
        self.verifyEqual(
            '<input type=hidden>',
            '<input Type=hidden>',
        )
        self.verifyNotEqual(
            '<input type=HIDDEN>',
            '<input TYPO=HIDDEN>',
        )
        self.verifyNotEqual(
            '<input type=hidden>',
            '<input TYPO=hide>',
        )

    def test_different_order_and_case(self):
        self.verifyEqual(
            '<IMG height=200 width=400>',
            '<img Width=400 Height=200>',
        )
        self.verifyNotEqual(
            '<img height=400 WIDTH=200>',
            '<Img width=400 HEIGHT=200>',
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_ignore_duplicate_keys(self):
        self.verifyEqual(
            '<input type=hidden type=input>',
            '<input type=hidden>',
        )
        self.verifyNotEqual(
            '<img type=input type=hidden>',
            '<Img type=hidden>',
        )
        self.verifyEqual(
            '<input TYPE=hidden type=input>',
            '<input type=hidden>',
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_valueless_keys(self):
        self.verifyEqual(
            '<input type=checkbox checked>',
            '<input checked type=checkbox>',
        )
        self.verifyNotEqual(
            '<img type=checkbox checked>',
            '<Img type=checkbox>',
        )
        self.verifyEqual(
            '<input type=checkbox checked>',
            '<input type=checkbox CHECKED>',
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_quotes(self):
        self.verifyEqual(
            '<input type="text">',
            '<input type=text>',
        )
        self.verifyNotEqual(
            '<img type="text">',
            '<Img type=hidden>',
        )
        self.verifyEqual(
            '''<input type=text placeholder='Hi there' value="Hi friend">''',
            '<input type=text value="Hi friend" placeholder="Hi there">',
        )
        self.verifyNotEqual(
            '<input type=text value="Hi there" placeholder="Hi friend">',
            '<input type=text value="Hi friend" placeholder="Hi there">',
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
