import unittest
import solution

class VerificationTestSuite(unittest.TestCase):
	def testWithAnotherInput(self):
		self.assertEqual(solution.functionToBeImplemented("secret sample input"), "secret expected output")
