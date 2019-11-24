import unittest
from tests.search import SearchTest
from tests.login import LoginTest
from tests.newslettersubscribe import NewsletterSubscribe
from tests.forgottenpassword import ForgottenPassword

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
newsletter_test = unittest.TestLoader().loadTestsFromTestCase(NewsletterSubscribe)
forgotten_pwd_test = unittest.TestLoader().loadTestsFromTestCase(ForgottenPassword)

test_suite = unittest.TestSuite([search_test, login_test, newsletter_test, forgotten_pwd_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
