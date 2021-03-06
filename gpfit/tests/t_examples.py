"""Unit testing of tests in docs/source/examples"""
import unittest
import os
import numpy as np
from gpkit.tests.helpers import generate_example_tests


class TestExamples(unittest.TestCase):
    """
    To test a new example, add a function called `test_$EXAMPLENAME`, where
    $EXAMPLENAME is the name of your example in docs/source/examples without
    the file extension.

    This function should accept two arguments (e.g. 'self' and 'example').
    The imported example script will be passed to the second: anything that
    was a global variable (e.g, "sol") in the original script is available
    as an attribute (e.g., "example.sol")

    If you don't want to perform any checks on the example besides making
    sure it runs, just put "pass" as the function's body, e.g.:

          def test_dummy_example(self, example):
              pass

    But it's good practice to ensure the example's solution as well, e.g.:

          def test_dummy_example(self, example):
              self.assertAlmostEqual(example.sol["cost"], 3.121)
    """

    def test_hoburgabbeel_ex6_1(self, example):
        """test_hoburgabbeel_ex6_1"""
        self.assertTrue(example.errorMA < 1e-2)
        self.assertTrue(example.errorSMA < 1e-4)
        self.assertTrue(example.errorISMA < 1e-5)


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
EXAMPLE_DIR = os.path.abspath(FILE_DIR + '../../../docs/source/examples')
# use gpkit.tests.helpers.generate_example_tests default: only default solver
TESTS = generate_example_tests(EXAMPLE_DIR, [TestExamples])


if __name__ == "__main__":
    from gpkit.tests.helpers import run_tests
    run_tests(TESTS)
