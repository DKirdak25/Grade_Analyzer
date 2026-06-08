class Analyzer():
				def __init__(self, marks):
								if not isinstance(marks, list) :
												raise TypeError("Marks must be only list ")
								if not marks:
												raise ValueError("list must not to be empty")
												
								self.marks = marks
								
				def average(self):
								return sum(self.marks) / len(self.marks)
								
				def lowest(self):
								return min(self.marks)
								
				def highest(self):
								return max(self.marks)
				
				def passed_students(self):
								passed = []
								for mark in self.marks:
												if mark >= 40:
																passed.append(mark)
								
								return len(passed)
	
												
												