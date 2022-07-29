import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testExample1(self):
		self.assertEqual(solution.functionToBeImplemented("sample input"), "expected output")
