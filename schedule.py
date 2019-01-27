#Evan DePosit
#New Beginnings
#capstone
# This file contains class data structures to store student information and functions to read that information from a file

#classes
class Student():
    def __init__(self, studentData):
        self.first= studentData[0]
        self.last= studentData[1]
        self.readingLevel= int(studentData[2])
        self.activityList= [] 

    def print_student(self):
        print('{} {} {} {} {}'.format('student: ', self.first, self.last, 'reading level: ', self.readingLevel))

class readingGroup():   
    def __init__(self, studentData):
        self.readingLevel
        self.studentList
        self.activityList=[]

class Teacher():
    pass

class ClassList():
    def __init__(self, classData):
        self.studentList=[]
        self.readingGroupList=[]

        for kid in classData:
            self.studentList.append(Student(kid))
        #what was this loop for?  accidently deleted
        #for student in self.studentList:

#class ReadingActivity(filePath):
    #pass
    
#file i/o functions
def read_teachers(filePath):
    #throw away first line or maybe use to determine day
    fin = open(filePath, 'rt')
    line=fin.readline() 
    #line=line[:-1:]
    print(line)

    teacherData=[]
    
    while True:
        #read in each student by line and count total
        line= fin.readline()
        if not line:
            break
        #line=line[:-1:]
        #print each line of student data
        print(line)
        
        #add to classData list
        #teacherData=line.split(',')
        #classData.append(studentData)
        
    fin.close()
    return classData    

def read_stu_file(filePath):
    studentCount=0
    columnCount=0 
    fin = open(filePath, 'rt')
   
    #count how many fields in csv
    line=fin.readline() 
    line=line[:-1:]
    #columnHeaders=[]
    #columnHeaders=line.split(',')
    #columnCount=len(columnHeaders)

    classData=[]
    
    while True:
        #read in each student by line and count total
        line= fin.readline()
        if not line:
            break
        line=line[:-1:]
        studentCount+=1
        #print each line of student data
        #print(line)
        
        #add to classData list
        studentData=line.split(',')
        classData.append(studentData)
        
    fin.close()
    return classData    

#main
filePath='test.csv'
#test data is read from file and placed in list
#csv <name>,<last>,<number> then list[1] == <last>
classTestData= read_stu_file(filePath)
print(classTestData) 

#test test student class constructor 
#input list[0] joe then student1.first == 'joe'
testStData=['joe', 'smith', 1]
student1= Student(testStData)
student1.print_student()

#test clastList class constructor
class1= ClassList(classTestData)

read_teachers('teacher.csv')
