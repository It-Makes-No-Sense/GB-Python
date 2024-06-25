import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2 * 2, 5, msg="Это не так работает.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
