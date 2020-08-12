import unittest
from parameterized import parameterized
from diagnostico1bis import CompuTools


class TestDiagnostico(unittest.TestCase):
    @parameterized.expand([
                            ([[1, 2, 3, 4]]),
                            ([[5, 6, 17, 8, 10]]),
                            ([[1, 3, 5, 17, 9, 11]]),
                            ([[5, 6, 17, 8, 9, 10, 11, 12]]),
                         ])
    def test_is_sorted(self, list):
        compu = CompuTools()
        self.assertTrue(compu.is_sorted(list))


    @parameterized.expand([
                            ([[1, 2, 3, 4]]),
                            ([[5, 6, 17, 18, 10]]),
                            ([[1, 3, 5, 17, 9, 11]]),
                            ([[5, 6, 17, 18, 9, 10, 11, 12]]),
                         ])
    def test_is_not_sorted(self, list):
        compu = CompuTools()
        self.assertFalse(compu.is_sorted(list))


if __name__== "___main___":
    unittest.main()
