import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.input_1 = [['Astralis', 2], ['Ninjas in Pyjamas', 1]]
        self.input_2 = [['Navi', 2], ['G2 Esports', 0]]
        self.input_3 = [['G2 Esports', 2], ['Vitality', 1]]
        self.input_4 = [['Ninjas in Pyjamas', 1], ['Vitality', 1]]
        self.input_5 = [['Astralis', 2], ['Navi', 1]]
        self.input_6 = [['Vitality', 2], ['Astralis', 0]]

        self.dict = {'Astralis': 0, 'Navi': 0, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}

        self.expected_1 = {'Astralis': 3, 'Navi': 0, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
        self.expected_2 = {'Astralis': 3, 'Navi': 3, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
        self.expected_3 = {'Astralis': 3, 'Navi': 3, 'G2 Esports': 3, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
        self.expected_4 = {'Astralis': 3, 'Navi': 3, 'G2 Esports': 3, 'Ninjas in Pyjamas': 1, 'Vitality': 1}
        self.expected_5 = {'Astralis': 6, 'Navi': 3, 'G2 Esports': 3, 'Ninjas in Pyjamas': 1, 'Vitality': 1}
        self.expected_6 = {'Astralis': 6, 'Navi': 3, 'G2 Esports': 3, 'Ninjas in Pyjamas': 1, 'Vitality': 4}


    def test_eq(self):
        self.assertDictEqual(h.point_analysis(self.dict, self.input_1), self.expected_1)
        self.assertDictEqual(h.point_analysis(self.dict, self.input_2), self.expected_2)
        self.assertDictEqual(h.point_analysis(self.dict, self.input_3), self.expected_3)
        self.assertDictEqual(h.point_analysis(self.dict, self.input_4), self.expected_4)
        self.assertDictEqual(h.point_analysis(self.dict, self.input_5), self.expected_5)
        self.assertDictEqual(h.point_analysis(self.dict, self.input_6), self.expected_6)


if __name__ == "__main__":
    unittest.main()