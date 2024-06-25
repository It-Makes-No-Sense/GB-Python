import io
import unittest
from unittest.mock import patch

from prime_unittest import is_prime


class TestPrime(unittest.TestCase):

    def test_id_prime(self):
        self.assertFalse(is_prime(42))
        self.assertTrue(is_prime(73))

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_false(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long time. Working...\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long time. Working...\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
