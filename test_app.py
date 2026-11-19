import unittest
from app import hitung_umur


class TestHitungUmur(unittest.TestCase):
    def test_umur_normal(self):
        self.assertEqual(hitung_umur(2004, 2026), 22)

    def test_umur_nol(self):
        self.assertEqual(hitung_umur(2026, 2026), 0)


if __name__ == "__main__":
    unittest.main()