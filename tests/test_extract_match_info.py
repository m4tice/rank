import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):

    def test_1_count_eq(self):
        self.assertCountEqual(h.extract_match_info("Astralis 2, Navi 1"), [["Astralis", 2], ["Navi", 1]])

    def test_1_list_eq(self):
        self.assertListEqual(h.extract_match_info("Astralis 2, Navi 1"), [["Astralis", 2], ["Navi", 1]])

    def test_2_count_eq(self):
        self.assertCountEqual(h.extract_match_info("Astralis 2, Team Vitality 1"), [["Astralis", 2], ["Team Vitality", 1]])

    def test_2_list_eq(self):
        self.assertListEqual(h.extract_match_info("Astralis 2, Team Vitality 1"), [["Astralis", 2], ["Team Vitality", 1]])

    def test_3_count_eq(self):
        self.assertCountEqual(h.extract_match_info("Astralis 2, Team Vitality 10"), [["Astralis", 2], ["Team Vitality", 10]])

    def test_3_list_eq(self):
        self.assertListEqual(h.extract_match_info("Astralis 2, Team Vitality 10"), [["Astralis", 2], ["Team Vitality", 10]])



if __name__ == "__main__":
    unittest.main()