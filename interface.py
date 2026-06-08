from logic import Analyzer

def get_student():
				print("Type 'q' to exit")
				marks = []
				while True:
								get_mark = input("Enter Marks of Student")
								
								if get_mark == "q":
												break
								elif get_mark == "":
												print("Empty not allowed try again")
												continue
								elif not get_mark.isdigit():
												print("only number are allowed")
												continue
								elif int(get_mark) < 0 :
												print("inavlid mark try again")
												continue
								elif int(get_mark) > 100:
												print("Marks cannot exceed 100")
												continue
								else:
												marks.append(int(get_mark))
				
				return marks
				
def main():
				marks = get_student()
				if not marks:
								print("No marks entered.")
								return
								
				grade_analyzer = Analyzer(marks)
				average = grade_analyzer.average()
				lowest = grade_analyzer.lowest()
				highest = grade_analyzer.highest()
				pass_students = grade_analyzer.passed_students()
				
				print(f" Average : {average}, \n Lowest : {lowest}, \n Highest : {highest}, \n Paased Students : {pass_students} ")
					
					
#if __name__ == "__main__":
#    main()
								