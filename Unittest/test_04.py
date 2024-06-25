import unittest


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
        self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()


if __name__ == '__main__':
    unittest.main(verbosity=2)
