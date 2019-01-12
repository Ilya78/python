import unittest
from client import *

class Testclient(unittest.TestCase):
    def test_presense(self):
        self.assertEqual(client('127.0.0.1',8888,'{"action": "presence", "time": "", "type": "status", "user": ""}'), b'{"response": "200", "alert": ""}')

    def test_probe(self):
        self.assertEqual(client('127.0.0.1',8888,'{"action": "probe", "time": "", "type": "status", "user": ""}'), b'{"response": "200", "alert": ""}')

    def test_json(self):
        self.assertEqual(client('127.0.0.1',8888,'test'), b'{"response": "400", "alert": ""}')

if __name__ == '__main__':
    unittest.main()
