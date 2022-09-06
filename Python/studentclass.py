class Student:
  """Define the Student based on their own identity that was chosen for them or they chose.
      Teacher, classes and such are defined by the school.
      Most schools don't care about age....COMMON SENSE IS EXPECTED TO UNDERSTAND THIS"""
  def __init__(self, school, name, ethnic):
    """Make the kid identifiable. Probably should use a birth certificate as a reference point too, but some unfortunate souls don't have that"""
    self.school = school
    self.name = name
    self.ethnic = ethnic
    self.classes = {}
    self.enrolled = True if school != "" else False

  def report(self, arg):
    """They may not physically speak, but this is the digital world. Everything is one function away...unless it's Python, in which you cannot do one liner functions non-annoyingly"""
    if arg.startswith('speak:'): print("[" + self.name + "]: " + arg.replace('speak:', '', 1))
    elif arg == 'name': print(self.name + " is introducing himself as...." + self.name + "! Wow, this sarcasm is much more effective in text! :DDD")
    elif arg == 'ethnic': print(self.name + " is " + self.ethnic + "~wait, they still exist?")
    elif arg == 'school':
      if self.school == "":
        print("Huh, did " + self.name + " get expelled or were they too smart for school in the first place? Guess better find out if they're under 18 or so, whether they're living in their parents house still or not.")
      else:
        print(self.name + " would like to let you all know that his school is..." + self.school + ". Not much is known, he/she/they tell me, but their grades and behavior is what would determine if it's good or not. Try contacting the school")
    else: print("Report parameter incorrect: Try seeing if the kid has much to value in the first place; we all already know those clowns that don't do much in their school career. Maybe " + self.name + " is one of them; most likely, but who knows.")    

class School:
  """Interface for student<->teacher interaction"""
  def __init__(self, name):
    self.name = name
    self.students = {}

  def expellStudent(self, studentName):
    """Highly debatable whether this is something that's right for teachers to have, but I'm confining myself to normal school standards"""
    self.students[studentName].enrolled = False
    self.students[studentName].school = ""

  def addStudent(self, studentInfo):
    """Let's see how long they last"""
    self.students[studentInfo.name] = studentInfo

  def reportCard(self, studentName):
    """Let's see the grades"""
    print(self.students[studentName].classes)

  def setGrades(self, studentName, grades):
    """Surprising if this isn't Fs, but try updating the internal School disctionary"""
    self.students[studentName].classes.update(grades)

school = School("Computer Programming Nerd Club: CPNC for short!")
maor = Student(school, "Maor", "Clown")
school.addStudent(maor)

maor.report("name")
school.setGrades(maor.name, {"Intro to Computer Programming": "F", "MCOMP104": "??"})
school.reportCard(maor.name)

maor.report("ethnic")
maor.report("speak:To gain proper humor, please insert the correct CDs~")
# Wait...did he just try to bring back a joke from 2010? Yeah, no, expelling. I don't care about the grades
school.expellStudent(maor.name)
maor.report("school")