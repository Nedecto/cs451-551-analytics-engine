import json
class GradeSet():
	def __init__(self, data = None):
		self.grades = []
		self.data = data
		if self.data != 'data/grade-data.json':
			raise Exception('Whoops')
		with open(self.data) as f:
			self.grades = json.loads(f.read())
		
		#Gives every letter a numerical value for later use in functions

		self.d = {'A':4,'B':3,'C':2,'D':1,'F':0}
	def avgGrade(self):
		"""
		This function takes the letter grade at index 3 and adds the earlier 
		established numerical value to count, where it is later divided by
		the total number of students. The average is converted into an int
		and compared against each value in the list of letters. Finally we 
		return our matching letter grade. 
		"""
		count = 0
		for i in self.grades:
			count += self.d[i[3]]
		avg = int(count/len(self.grades))
		for i in self.d:
			if self.d[i] == avg:
				return i 
	def difGrade(self):
		"""
		This function takes the sum of every change in letter grade and
		adds each change to a corresponding amount.
		EX. a change from 'C' to 'A' is 2 just as 'D' to 'B' is also 2
		It then returns the average number in grade changes

		"""
		f = {4:0,3:0,2:0,1:0,0:0}
		for i in self.grades:
			diff = abs(self.d[i[2]] - self.d[i[3]])
			f[diff] += 1
			
		h = 0
		l = 0
		for i in range(1, len(f)):
			if f[i] != 0:
				l += f[i]
			h += f[i]*i

		return int(h/l)

	def cgrade(self):
		"""
		This function adds a one to each corresponding letter grade 
		found at index 3 of your json file
		"""
		f = {'A':0,'B':0,'C':0,'D':0,'F':0}
		for i in self.grades:
			f[i[3]] += 1
		return f
	def mf(self):
		"""
		This function adds a one for each corresponding letter at index 1
		of your json file
		"""
		f = {'M':0,'F':0}
		for i in self.grades:
			f[i[1]] += 1
		return f


