#   unittest
from unittest import TestLoader, TestSuite
#   pyunitreport
from pyunitreport import HTMLTestRunner
#   Files
from assertions import AssertionsTests
from search_tests_assertions import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)
#   Suite test building
smoke_test = TestSuite([assertions_test, search_test])
#   For reports generation
kwargs = {
    "output": 'smoke-report'
}

#*   Runner stores a report generated for HTMLTestRunner with the keywordarguments(kwargs)
runner = HTMLTestRunner(**kwargs)
#   Runs the test suit
runner.run(smoke_test)
