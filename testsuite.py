import unittest

from tests.search import SearchTest
from tests.login import LoginTest
from tests.newslettersubscribe import NewsletterSubTest
from tests.forgottenpassword import ForgotPwdTest
from tests.passwordchange import PwdChangeTest
from tests.createacc import CreateAccTest


search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
newsletter_test = unittest.TestLoader().loadTestsFromTestCase(NewsletterSubTest)
forgotten_pwd_test = unittest.TestLoader().loadTestsFromTestCase(ForgotPwdTest)
pwd_change_test = unittest.TestLoader().loadTestsFromTestCase(PwdChangeTest)
create_acc_test = unittest.TestLoader().loadTestsFromTestCase(CreateAccTest)

test_suite = unittest.TestSuite([search_test, login_test, newsletter_test, forgotten_pwd_test, pwd_change_test, create_acc_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
