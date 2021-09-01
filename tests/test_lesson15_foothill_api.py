import json
import unittest
import requests
from parameterized import parameterized


class FoothillApiTests(unittest.TestCase):
    def get_foothill_course_search(self):
        return requests.get(url='https://catalog.foothill.edu/course-search/')

    # '''
    # curl 'https://catalog.foothill.edu/course-search/api/?page=fose&route=search&keyword=math' \
    #   -H 'Connection: keep-alive' \
    #   -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    #   -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    #   -H 'X-Requested-With: XMLHttpRequest' \
    #   -H 'sec-ch-ua-mobile: ?0' \
    #   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
    #   -H 'Content-Type: application/json' \
    #   -H 'Origin: https://catalog.foothill.edu' \
    #   -H 'Sec-Fetch-Site: same-origin' \
    #   -H 'Sec-Fetch-Mode: cors' \
    #   -H 'Sec-Fetch-Dest: empty' \
    #   -H 'Referer: https://catalog.foothill.edu/course-search/' \
    #   -H 'Accept-Language: en-US,en;q=0.9' \
    #   --data-raw '%7B%22other%22%3A%7B%22srcdb%22%3A%22%22%7D%2C%22criteria%22%3A%5B%7B%22field%22%3A%22keyword%22%2C%22value%22%3A%22math%22%7D%5D%7D' \
    #   --compressed
    # '''

    def post_foothill_course_search(self, keyword=None, page=None, route=None, payload=None, **params):
        default_params = {
            'page': page or 'fose',
            # 'page': page if page is not None else None,
            'route': route or 'search',
            'keyword': keyword
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json'
        }
        json = {
            'other': {'srcdb': ''},
            'criteria': [
                {'field': 'keyword', 'value': keyword}
            ]
        }


        params = params if params is not None else default_params

        data = payload if payload is not None else json

        return requests.post(url='https://catalog.foothill.edu/course-search/api/',
                             params=params, headers=headers, json=data)

    def test_foothill_catalog_api(self):
        response = self.get_foothill_course_search()
        self.assertEqual(200, response.status_code)
        self.assertIn('/course-search/', response.url)

        self.assertIn('COURSE SEARCH', response.text)

    def test_search_course_catalogue(self):
        result = self.post_foothill_course_search('math')
        search_results = json.loads(result.text).get('results')
        # 1 option (good way for checking one course):
        # found = False
        # for i in search_results:
        #     if i.get('code') == 'MATH 180':
        #         found =True
        #         break
        # self.assertTrue(found, "MATH 180 not found")

        # 2 option
        # for i in search_results:
        #     if i.get('code') == 'MATH 180':
        #         break
        # else:
        #     self.fail('MATH 180 not found')

        # 3 option
        # for i in search_results:
        #     if i.get('code') == 'MATH 180':
        #         break
        # else:
        #     assert False, "MATH 180 not found"

        # 4option (better option for checking multiply courses there):
        classes = list(x.get('code') for x in search_results)
        self.assertIn('MATH 180', classes)
        self.assertIn('MATH 10', classes)

        # 5option to get title of the courses:
        # classes = list({x.get('code'): x.get('title')} for x in search_results)
        # # print(classes)

    @parameterized.expand([
        ('no_keyword', None, None, None, '{"fatal":"criterion.value is null"}'),
        ('bad_route', 'art', 'BAD', None, '{"fatal":"Unknown route \\"BAD\\""}')
    ])

    def test_negative_tests(self, test_name, keyword, route, page, expected_output):
        result = self.post_foothill_course_search(keyword, page, route)
        self.assertEqual(expected_output, result.text)

    def test_search_no_keyword(self):
        result = self.post_foothill_course_search(keyword=None)
        self.assertEqual('{"fatal":"criterion.value is null"}', result.text)

    def test_search_bad_route(self):
        result = self.post_foothill_course_search(keyword='art', route='BAD')
        self.assertEqual('{"fatal":"Unknown route \\"BAD\\""}', result.text)
    #
    # def test_search_empty_page(self):
    #     result = self.post_foothill_course_search(keyword='art', page=' ')
    #     self.assertEqual('', result.text)
    #
    # def test_search_bad_payload(self):
    #     payload = {}
    #     result = self.post_foothill_course_search(keyword='art', payload=payload)
    #     self.assertEqual('{"fatal":"searchData.other is undefined"}', result.text)
    #
    # def test_search_partial_payload(self):
    #     keyword = 'art'
    #     payload = {'other': {'db': ''},
    #                'criteria': [
    #                    {'field': 'keyword', 'value': keyword}
    #                ]
    #                }
    #     result = self.post_foothill_course_search(keyword=keyword, payload=payload)
    #     self.assertEqual('', result.text)
    #
    # def test_search_bad_params(self):
    #     result = self.post_foothill_course_search(fruit='kiwi', boy="male")
    #     self.assertEqual('', result.text)
    #


    def test_search_no_keyword(self, test_name, keyword, route, page, expected_output):
        result = self.post_foothill_course_search(keyword, page, route)
        self.assertEqual(expected_output, result.text)

    def test_search_bad_route(self):
        result = self.post_foothill_course_search(keyword='art', route='BAD')
        self.assertEqual('{"fatal":"Unknown route \\"BAD\\""}', result.text)

    def test_search_empty_page(self):
        result = self.post_foothill_course_search(keyword='art', page=' ')
        self.assertEqual('', result.text)

    def test_search_bad_payload(self):
        payload = {}
        result = self.post_foothill_course_search(keyword='art', payload=payload)
        self.assertEqual('{"fatal":"searchData.other is undefined"}', result.text)

    def test_search_partial_payload(self):
        keyword = 'art'
        payload = {'other': {'db': ''},
            'criteria': [
                {'field': 'keyword', 'value': keyword}
            ]
        }
        result = self.post_foothill_course_search(keyword=keyword, payload=payload)
        self.assertEqual('', result.text)

    def test_search_bad_params(self):
        result = self.post_foothill_course_search(fruit='kiwi', boy="male")
        self.assertEqual('', result.text)


if __name__ == '__main__':
    unittest.main()
