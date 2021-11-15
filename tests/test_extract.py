import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):

    def setUp(self):
        self.input = "./data/sample-input-test.txt"
        self.expected = [[['Astralis', 2], ['Ninjas in Pyjamas', 1]],
                        [['Astralis', 1], ['Navi', 1]],
                        [['Navi', 2], ['G2 Esports', 0]],
                        [['G2 Esports', 2], ['Vitality', 1]],
                        [['Ninjas in Pyjamas', 2], ['Vitality', 0]]]

    def test_1_count_eq(self):
        self.assertCountEqual(h.extract(self.input), self.expected)

    def test_1_list_eq(self):
        self.assertListEqual(h.extract(self.input), self.expected)


if __name__ == "__main__":
    unittest.main()