import addit
import unittest

class Addtest(unittest.TestCase):

    def additiontest(self):
        assert addit.puttogether(2,3)  == True

    if __name__ == "__main__":
        unittest.main()


