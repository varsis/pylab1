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
        self.courseMarks[course] = mark
        """ 
        Adds a course mark to the current Student
        >>> student = Student('test','last')
        
        >>> student.addCourseMark('test',100)
        
        >>> student.courseMarks
        {'test': 10}
        """
    
    # get the average for all listed course marks
    def average(self):
        return sum(self.courseMarks, 0.0) / len(self.courseMarks)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()