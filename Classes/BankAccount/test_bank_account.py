import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(12345, 'John Doe', 1000)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(100), 1100)
        self.assertEqual(self.account.deposit(-100), 0)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(100), 900)
        self.assertEqual(self.account.withdraw(-100), 0)
        self.assertEqual(self.account.withdraw(2000), 0)

    def test_transfer(self):
        self.assertEqual(self.account.transfer(100), 0) # Transfer is not implemented

    def test_get_account_balance(self):
        self.assertEqual(self.account.get_account_balance(), '1000')

    def test_get_account_details(self):
        self.assertEqual(self.account.get_account_details(), '12345 John Doe 1000')

if __name__ == '__main__':
    unittest.main()

