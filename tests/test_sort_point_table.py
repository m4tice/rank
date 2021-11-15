import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):

    def setUp(self):
        self.input = {'Astralis': 6, 'Navi': 3, 'G2 Esports': 3, 'Ninjas in Pyjamas': 1, 'Vitality': 4}
        self.expected = [['Astralis', 6], ['Vitality', 4], ['G2 Esports', 3], ['Navi', 3], ['Ninjas in Pyjamas', 1]]

    def test_1_count_eq(self):
        self.assertCountEqual(h.sort_point_table(self.input), self.expected)

    def test_1_list_eq(self):
        self.assertListEqual(h.sort_point_table(self.input), self.expected)


if __name__ == "__main__":
    unittest.main()