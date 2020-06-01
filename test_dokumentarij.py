import unittest
from dokumentarij import DokumentarijView

class dokumentarijTestCase(unittest.TestCase):
    def test_new_name(self):
        game_test = DokumentarijView()
        name_one = game_test.get_new_name()
        name_two = game_test.get_new_name()
        self.assertNotEqual(str(name_one), str(name_two), "Imena moraju biti različita")



if __name__ == "__main":
    unittest.main()