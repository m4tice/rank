import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.input = [[['Astralis', 2], ['Ninjas in Pyjamas', 1]],
                        [['Astralis', 1], ['Navi', 1]],
                        [['Navi', 2], ['G2 Esports', 0]],
                        [['G2 Esports', 2], ['Vitality', 1]],
                        [['Ninjas in Pyjamas', 2], ['Vitality', 0]]]

        self.expected = {'Astralis': 0, 'Navi': 0, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}


    def test_eq(self):
        self.assertDictEqual(h.create_table_dict(self.input), self.expected)


if __name__ == "__main__":
    unittest.main()