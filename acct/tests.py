from django.test import TestCase

from .models import AccountType


class AccountTypeTests(TestCase):

    def test_always_pass(self):
        """
        Simple test to allow tests to be run automatically
        """
        db = AccountType()
        print(db)
        case = True
        self.assertIs(case, True)
