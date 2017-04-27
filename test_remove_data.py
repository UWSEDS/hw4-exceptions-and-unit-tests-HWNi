import unittest
import os
from get_remove_data import remove_data

url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
filename = '4xy5-26gy.csv'

class TestRemoveData(unittest.TestCase):
    # test the case of removing file that is present locally
    def testFileExists(self):
        if not os.path.exists(filename):
            f = open(filename, "wb")
            f.close()
        result = remove_data(url)
        expect = "Remove succeeds"
        self.assertEqual(result, expect)

    # test the case that local file does not exist
    def testFileNotExists(self):
        if os.path.exists(filename):
            os.remove(filename)
        result = remove_data(url)
        expect = 'Local file does not exist'
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()