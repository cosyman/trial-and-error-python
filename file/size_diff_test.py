__author__ = 'ltyao'

import unittest
from size_diff import cmp_size


class SizeTestCase(unittest.TestCase):
    def setUp(self):
        self.left_dir = "D:\Users\ltyao\PycharmProjects\untitled5\NET_1367635\ws.mobilesecure.payment.soa2\payment"
        self.right_dir = "D:\Users\ltyao\PycharmProjects\untitled5\NET_1368884\ws.mobilesecure.payment.soa2\payment"

    def test_echo(self):
        cmp_size(self.left_dir, self.right_dir)
        print("--------------------")
        cmp_size(self.right_dir, self.left_dir)


if __name__ == '__main__':
    unittest.main()
