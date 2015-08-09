import unittest
from my_script import is_palindrome

class KnownInput(unittest.TestCase):
    knownValues = (('lego', False),
            ('radar', True))

    def testKnownValues(self):
        for word, palin in self.knownValues:
            result = is_palindrome(word)
            self.assertEqual(result, palin)
