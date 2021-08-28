import unittest
import requests


class FoothillApiTests(unittest.TestCase):
    def test_foothill_catalog_api(self):
        response = requests.get(url='https://catalog.foothill.edu/course-search/')
        self.assertEqual(200, response.status_code)
        self.assertIn('/course-search/', response.url)

        self.assertIn('COURSE SEARCH', response.text)


if __name__ == '__main__':
    unittest.main()
