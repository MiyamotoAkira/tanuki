#
# Call Flow
# GET:host
# Should return a list of all the possible options
# This will be returned as hypermedia
# Current options should be
# GET:"/all" (whatever the url) will return you all the toggles
# GET:"/group/{groupResourceIdentifier}" will return you the toggles for that specific group
# GET: "/on" will return you all the toggles that are currently on.
# GET: "/off" will return you all the toggles that are currently off.

# groupResourceIdentifier is calculated on the fly based on the possible options of collating groups
# resourceIdentifer maybe on the fly as well?

# All the above will accept a query parameter called "max_entries", which will limit the number of entries that will appear on the answer. If "max_entries" is specified links to "next", "previous", "first" and "last" will be provided.
# A header request (or query parameter) of "embedded" will provide the full information of all the toggles -- Needs to be query parameter so it appears on the links when max_entries is present.
# All the above will be sorted alphabetically


# Results provided
#
# GroupResourceIdentifer (if present)
# ToggleCollection:(for each)
#    Name
#    Status (on or off)
#    Links:
#        Self
# Links:
#    Self
#    First (if max_entries was specified)
#    Previous (if max_entries was specified)
#    Next (if max_entries was specified)
#    Last (if max_entries was specified)
#
# Embedded: (if requested)
#     Toggles: (foreach)
#         (Check single below)

# POST: "/" Used to create a new toggle. By default it will be switched off
# GET: "/{toggleId}"
# POST: "/{toggleId}/switch

# Results provided

# For single
# Name
# Groups: (for each)
#    Name
# Status (on or off)
# Links:
#   Self
#   Get
#   Switch OFF
#   or
#   Switch ON
#   Modify

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
