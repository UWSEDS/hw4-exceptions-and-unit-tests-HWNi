import unittest
import os
from get_remove_data import get_data

url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
filename = '4xy5-26gy.csv'

class TestGetData(unittest.TestCase):
    # test the case that file is present locally
    def testFileExists(self):
        if not os.path.exists(filename):
            f = open(filename, "wb")
            f.close()
        expect = 'File exists'
        result = get_data(url)
        self.assertEqual(result, expect)

    # test the case that file is not present locally but URL points to a file that exists
    def testURLExists(self):
        if os.path.exists(filename):
            os.remove(filename)
        expect = 'No local file but URL exists'
        result = get_data(url)
        self.assertEqual(result, expect)

    # test the case that URL does not point to a file that exists
    def testURLNotExists(self):
        if os.path.exists(filename):
            os.remove(filename)
        invalidUrl = 'https://data.ciattle.gov/resource/4xy5-2.csv'
        expect = "URL does not exist"
        result = get_data(invalidUrl)
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()