import unittest
from grades import GradeSet
class test_grade_data(unittest.TestCase):
	def test_init(self):
		a = GradeSet('data/grade-data.json')
		
	def test_init2(self):
		with self.assertRaises(Exception) as context:
			GradeSet('asdfasdfasdf')
		self.assertTrue('Whoops' in str(context.exception)) #python3 requires it to be in str format
		
	def test_avgGrade(self):
		a = GradeSet('data/grade-data.json')
		self.assertEqual('B', a.avgGrade())
		
	def test_difGrade(self):
		a = GradeSet('data/grade-data.json')
		self.assertEqual(1, a.difGrade())
		
	def test_cgrade(self):
		a = GradeSet('data/grade-data.json')
		self.assertEqual(43, a.cgrade()['A'])
		
	def test_mf(self):
		a = GradeSet('data/grade-data.json')
		self.assertEqual(17, a.mf()['F'])
		
if __name__ == '__main__':
	unittest.main()