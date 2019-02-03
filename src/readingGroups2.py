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
    def __init__(self, first, last):
       self.first
       self.last
       self.availableTimes=[]

class ClassList():
    def __init__(self, studentData, teacherData):
        #add number of days in week
        #start and stop times
        self.studentList=[]
        self.readingGroupList=[]
        self.staffList=[]

        for kid in studentData:
            self.studentList.append(Student(kid))
        #what was this loop for?  accidently deleted.  REading groups.
        #for student in self.studentList:
        
        #for teacher in teacherData:
                            

#class ReadingActivity(filePath):
    #pass
    
#file i/o functions
#maybe this should just be part class above teachers, teacher list teacher schedule?
#if so add pattern matching to identify how many in/out times for eac day
def read_teachers(filePath):
    #throw away first line or maybe use to determine day
    fin = open(filePath, 'rt')
    line=fin.readline() 
    #line=line[:-1:]
    #print(line)

    teacherData=[]
    
    teacherDataList=[]
    while True:
        #read in each student by line and count total
        line= fin.readline()
        if not line:
            break
        #line=line[:-1:]
        #print each line of student data
        #print(line)
        
        #add to teacherData list
        teacherData=line.split(',')
        teacherDataList.append(teacherData)
    
    fin.close()
    #print(teacherDataList)
    return teacherDataList 

def teacher_sched(teacherTimes):
    #input: list of strings each string lis line from teacher schedule file
    #output list of teacher objects
    #start by just making general schedule for one day/all week
    teacherList=[]
    print('teacherTimes list')
    print(teacherTimes)
    print()
    print()
    #orgainize teacher schedule by teacher or day?  teacher
    #count how many days in schedule and how many in/out times in day from file
    #need to have class set up before this point
    dayCount=4
    inOutCount=4
    for line in teacherTimes:
        #list of days, each day is list of in/out lists
        dayList=[]
        name =line.pop(0)
        #list of days, each day is list of time chunks which is list  clockin/out times
        #hard coded, need to add functions
        dayCount=4
        inOutCount=2
        #loop for each day
        for i in range(0, dayCount):
            #each day is list of in/out times
            #dayList[i]=[]
            dayList.append([])
            #get each time that teacher enters/leaves class in one day
            for j in range(0, inOutCount):
                #get in and out Time as string
                inTimeStr=line.pop(0)
                outTimeStr=line.pop(0) 
                #convert int time to min int times with function
                #need handling for empty strngs if:else intime=NONE
                inOut=[]
                if(inTimeStr):
                    inTime=time_to_min(inTimeStr)
                    outTime=time_to_min(outTimeStr)
                    #add to list tuple list
                    inOut.append(inTime)
                    inOut.append(outTime)
                    #add to tuple to lis day list
                dayList[i].append(inOut) 

        #test data is there before running it through teacher init
        print(name)
        #print each day
        for i in range(0, dayCount): 
            print('day', i)
            for j in range(0, inOutCount):
            #for j in range(0, len(dayList[i])):
                if(dayList[i][j]):
                    print('In: ', dayList[i][j][0])
                    print('Out: ', dayList[i][j][1])
                    
    return

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

def min_to_time(minTime):
    print()
    print('time= ', minTime)

    minutes=minTime%60
    hour=int(minTime/60)
    print('hour= ', hour)
    print('minutes= ', minutes)
    
    if hour == 12:
        timeOfDay='PM'
    elif hour > 12:
        timeOfDay='PM'
        hour= hour-12
    else:
        timeOfDay='AM'    
    
    time=str(hour) + ':' + str(minutes) + ' ' + timeOfDay
    print('time= ', time)
    return time 

def time_to_min(time):
    #input time as string
    #output time as minutes
    #test cases
    minutes=999 

    fields= time.split(':')
    #print()
    #print(fields)
    
    #get hour first
    hourStr=fields.pop(0)
    hour=int(hourStr)

    #start by getting time of day from last string in list iff there at all
    if (('am' in fields[-1]) or ('AM' in fields[-1])):
        #print('its morning')
        timeOfDay= 0
    elif(('pm' in fields[-1]) or ('PM' in fields[-1]) and (hour !=12)):
        #print("it's the afternoon")
        #time of day equals minutes that happened in morning that need to be added
        timeOfDay=720
    else:
        #print('no time of day info in string')
        timeOfDay=None 
        
    minStr=fields.pop(0)

    #print('hour string= ', hourStr)
    #print('minutes string= ', minStr)
    #if timeOfDay is not None:
        #print('time of day: ', timeOfDay)
    
    #get numbers from sting
    minutes= int(minStr[:2:])

    #print('hour int=', hour)
    #print('minutes int= ', minutes)
    #print('remaining minutes', minStr)
    if timeOfDay is None:
        if(hour >=1 and hour< 7):
            minutes= ((hour +12)*60)+ minutes
        else:
            minutes= (hour*60)+minutes
    else:
        minutes =(60 * hour) + minutes + timeOfDay

    #print('total minutes', minutes)
    return minutes

#main
filePath='test.csv'
#test data is read from file and placed in list
#csv <name>,<last>,<number> then list[1] == <last>
classTestData= read_stu_file(filePath)
#print(classTestData) 

#test test student class constructor 
#input list[0] joe then student1.first == 'joe'
testStData=['joe', 'smith', 1]
student1= Student(testStData)
#student1.print_student()

read_teachers('teacher.csv')
testTeacherData= read_teachers('teacher.csv')
#print(testTeacherData)
teacher_sched(testTeacherData)

#test clastList class constructor
#class1= ClassList(classTestData, testTeacherData)

#turn times from 12 to 24 then to decimal
#time_to_min('12:30:00 PM')
#time_to_min('9:30 AM')
#time_to_min('10:30')
#time_to_min('2:30')

min_to_time(750)
min_to_time(570)
min_to_time(630)
min_to_time(870)
