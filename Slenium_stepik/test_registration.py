from registration import *
import unittest


class Test_reg(unittest.TestCase):
    """Initialization test class"""

    def test_reg1(self):
        test_link = "https://suninjuly.github.io/registration1.html"
        self.assertEqual(reg(test_link), "Congratulations! You have successfully registered!", "Failed first test")

    def test_reg2(self):
        test_link = "https://suninjuly.github.io/registration2.html"
        self.assertEqual(reg(test_link), "Congratulations! You have successfully registered!", "Failed second test")
        print("sadsaasd")

if __name__ == "__main__":
    unittest.main()