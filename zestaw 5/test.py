import fracs
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self): pass

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([4, 5], [1, 2]), [13, 10])
        self.assertEqual(fracs.add_frac([-1, -10], [-3, 4]), [-13, 20])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 10], [3, 4]), [-13, 20])
        self.assertEqual(fracs.sub_frac([3, 5], [-3, 2]), [21, 10])
        self.assertEqual(fracs.sub_frac([6, 7], [3, 8]), [27, 56])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([6, 7], [3, 8]), [9, 28])
        self.assertEqual(fracs.mul_frac([3, 8], [-2, 6]), [-1, 8])
        self.assertEqual(fracs.mul_frac([56, 34], [2, -7]), [-8, 17])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([56, 34], [2, 7]), [98, 17])
        self.assertEqual(fracs.div_frac([8, 9], [1, 3]), [8, 3])
        self.assertEqual(fracs.div_frac([3, 90], [3, 67]), [67, 90])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1,2]), True)
        self.assertEqual(fracs.is_positive([-1,2]), False)
        self.assertEqual(fracs.is_positive([-1,-2]), True)
        self.assertEqual(fracs.is_positive([1,-2]), False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([0, 0]), True)
        self.assertEqual(fracs.is_zero([0, 2]), True)
        self.assertEqual(fracs.is_zero([0, 4]), True)
        self.assertEqual(fracs.is_zero([0, 1]), True)
        self.assertEqual(fracs.is_zero([1, 1]), False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 4]), 1)
        self.assertEqual(fracs.cmp_frac([2, 4], [1, 2]), 0)
        self.assertEqual(fracs.cmp_frac([2, 4], [2, 3]), -1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 1/2)
        self.assertEqual(fracs.frac2float([3, 4]), 3/4)
        self.assertEqual(fracs.frac2float([-1, 8]), -1/8)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
