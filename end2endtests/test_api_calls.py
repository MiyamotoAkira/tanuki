#
# Call Flow
# GET:host
# Should return a list of all the possible options
# This will be returned as hypermedia
# Current options should be
# GET:"/all" (whatever the url) will return you all the toggles
# GET:"/group/{groupname}" will return you the toggles for that specific group
# GET: "/on" will return you all the toggles that are currently on
# GET: "/off" will return you all the toggles that are currently off.
# POST: "/"
# All the four above will accept a query parameter called "max_entries", which will limit the number of entries that will appear on the answer. If "max_entries" is specified links to "next", "previous", "first" and "last" will be provided
# All the four above will be sorted alphabetically

# Improvements
# Provide a search option, maybe through a query parameter? or should be a sub resource?

import requests
import unittest

class TestCreationPaths(unittest.TestCase):
    def test_happy_creation_path(self):
        r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.headers['content-type'], 'application/json; charset=utf8')
        self.assertEqual(r.encoding, 'utf-8')
        #r.text

        #r.json()
