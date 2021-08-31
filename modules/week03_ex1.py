class Student():
    """A student"""

    def __init__(self, name, gender, data_sheet, image_url):
        """Initializes a student with a name, gender, data sheet and image"""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        """Gets average grade"""
        grades = self.data_sheet.get_grades_as_list()
        return round((sum(grades) / len(grades)), 2)
    
    def get_study_progression(self):
        """Gets the student's study progression in percentage (%)"""
        return (self.data_sheet.get_all_ects() / 150) * 100
    
    def get_courses(self):
        """Gets the students courses in a list"""
        return self.data_sheet.courses

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def __str__(self):
        return '%r is a %r student. %r. Image URL: %r' % (self.name, self.gender, self.data_sheet, self.image_url)


class DataSheet():
    """A data sheet with multiple courses in particular order"""

    def __init__(self, courses):
        """Initializes a data sheet with its courses"""
        self.courses = courses

    def get_grades_as_list(self):
        """Gets grades as list"""
        return [course.grade for course in self.courses]
    
    def get_all_ects(self):
        """Gets ECTs from all courses"""
        return sum(course.ECTS for course in self.courses)

    def __repr__(self):
        return 'Datasheet(%r)' % (self.courses)

    def __str__(self):
        return 'Courses attended: %r' % (self.courses)


class Course():
    """A course"""

    def __init__(self, name, classroom, teacher, ETCS, grade):
        """Initializes a course with a name, classroom, teacher, ETCS and optional grade if the course is taken"""
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ETCS
        self.grade = grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)

    def __str__(self):
        return '%r in %r with %r. ETCs for the course: %r. Grade: %r' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)