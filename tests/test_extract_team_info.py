import unittest
import rank.helper as h


class TestListElements(unittest.TestCase):

    def test_1_count_eq(self):
        self.assertCountEqual(h.extract_team_info("Astralis 2"), ["Astralis", 2])

    def test_1_list_eq(self):
        self.assertListEqual(h.extract_team_info("Astralis 2"), ["Astralis", 2])

    def test_2_count_eq(self):
        self.assertCountEqual(h.extract_team_info("Team Vitality 2"), ["Team Vitality", 2])

    def test_2_list_eq(self):
        self.assertListEqual(h.extract_team_info("Team Vitality 2"), ["Team Vitality", 2])

    def test_3_count_eq(self):
        self.assertCountEqual(h.extract_team_info("Team Vitality 10"), ["Team Vitality", 10])

    def test_3_list_eq(self):
        self.assertListEqual(h.extract_team_info("Team Vitality 10"), ["Team Vitality", 10])


if __name__ == "__main__":
    unittest.main()