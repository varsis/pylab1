class Student:
    courseMarks={}
    name=""
    family=""
    
    # Initialize a student
    def __init__(self, name, family):
        self.name = name;
        self.family = family;
    
    #Add a course mark
    def addCourseMark(self, course, mark):
	"""
	Test add course mark
	>>> s.addCourseMark("cmput410",100)
	>>> s.courseMarks
	{'cmput410': 100}
	>>> s.addCourseMark("cmput410",105)
	Course mark must be >= 0 and <= 100
	>>> s.courseMarks
	{'cmput410': 100}
	"""
	if (mark <= 100 and mark >= 0):
    		self.courseMarks[course] = mark
	else:
    		print("Course mark must be >= 0 and <= 100")
		
    
    # get the average for all listed course marks
    def average(self):
	"""
	Test average
	>>> s.addCourseMark("cmput410",60)
	>>> s.addCourseMark("cmput420",60)
	>>> s.average()
	60.0
	>>> s.addCourseMark("cmput400",0)
	>>> s.average()
	40.0
	"""
        return sum(self.courseMarks.values(), 0.0) / len(self.courseMarks)

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'s': Student('name','family')})
