import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):

    def setUp(self):
        self.input = [[['Astralis', 2], ['Ninjas in Pyjamas', 1]],
                        [['Navi', 2], ['G2 Esports', 0]],
                        [['G2 Esports', 2], ['Vitality', 1]],
                        [['Ninjas in Pyjamas', 1], ['Vitality', 1]],
                        [['Astralis', 2], ['Navi', 1]],
                        [['Vitality', 2], ['Astralis', 0]]]
        
        self.expected = [['Astralis', 6, 1], ['Vitality', 4, 2], ['G2 Esports', 3, 3], ['Navi', 3, 3], ['Ninjas in Pyjamas', 1, 5]]

    def test_1_count_eq(self):
        self.assertCountEqual(h.transform(self.input), self.expected)

    def test_1_list_eq(self):
        self.assertListEqual(h.transform(self.input), self.expected)


if __name__ == "__main__":
    unittest.main()