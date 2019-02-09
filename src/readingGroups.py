#Evan DePosit
#New Beginnings
#capstone
#This file contains class data structures to store student information and functions to read that information from a file

#classes
class Event():
    def __init__(self, day, startStop):
        self.startStop=startStop
        self.day= day
        #can be either pointer to one student or group of students
        self.students=None

class Group_Lesson(Event):
    def __init__(self, teacher, day, startStop):
        super().__init__(day, startStop)
        self.teacher=teacher
    
class Class_Schedule():
    def __init__(self, teacherSchedule, classList, scheduleTimes):
        self.teacherSchedule=teacherSchedule
        self.classList=classList
        #schedule times is schedule_parameters object
        #change to list of schedule_paramters objects, one for each day
        self.schedParams=scheduleTimes  
        masterGroupActList=[]
        masterGroupEventList=[]
        
    #generate activity list for each readingGroup 
    def make_reading_group_act():
        pass

    def make_reading_lessons(self):
    #input:self used to access teacher objects
    #output: creates event, adds it to list for teachers and master events list
        weekLen= self.schedParams.days
        for teacher in self.teacherSchedule.teacherList:        
            print(teacher.name)
            for day in range(0, weekLen):    
                #function that returns list of in/out times for day
                times= teacher.get_days_inOuts(day)
                print('day ', day)
                print(times)
                #get length of days
                #interate over list of inout times`
                for inOut in times:
                    if inOut:
                        print(inOut[0])
                        print(inOut[1])
                        #compare in/out times to see if it matches up with events 
                        #if times matche create event
                            #create event
                            #add to teachers list
                            #add to master list

        #go through each groups activity list and add it to master list

        #use schedule Times and teacher schedule to generage reading group events

        #add teacher events to masterEventList

    #run teacherEvents through max match algorithm

class Schedule_Parameters():
    def __init__(self, days, actPerDay, duration, start1, end1, start2=None, end2=None):
    #def __init__(self, days, actPerDay, duration):
        self.days=days
        self.actPerDay=actPerDay
        self.duration = duration
        #list of of days, each day is  list of start and stop times
        self.eventTimes=[]

    #def set_events_times(day, start1, end1, start2=None, end2=None)
         
        self.start1=start1
        self.end1= end1
        self.start2=start2
        self.end2=end2

        event=0
        periodStart=self.start1
        periodEnd=self.end1
        actStart=None
        actEnd=None
        nonScheduled=self.actPerDay 
        #figure out how many activities in first time chunk
         
        actInPeriod=int((periodEnd-periodStart)/self.duration)
        while(actInPeriod and nonScheduled):   
            actStart=periodStart
            actEnd= periodStart+self.duration
            #add atart and end times to event times list 
            startEnd=[]
            startEnd.append(actStart)
            startEnd.append(actEnd)
            self.eventTimes.append(startEnd)
            #update variables for next time through loop
            nonScheduled=nonScheduled-1
            #print('start: ', actStart)
            #print('end: ', actEnd)
            #print(startEnd)
            #print('remaining events to plan: ', nonScheduled)
            #add to list of event times
            periodStart= actEnd           
            actInPeriod=int((periodEnd-periodStart)/self.duration)
             
        if(nonScheduled and self.start2):
            periodStart=self.start2
            periodEnd=self.end2
            actStart=None
            actEnd=None
            
            actInPeriod=int((periodEnd-periodStart)/self.duration)
            while(actInPeriod and nonScheduled):   
                actStart=periodStart
                actEnd= periodStart+self.duration
                #add atart and end times to event times list 
                startEnd=[]
                startEnd.append(actStart)
                startEnd.append(actEnd)
                self.eventTimes.append(startEnd)
                #update variables for next time through loop
                nonScheduled=nonScheduled-1
                #print('start: ', actStart)
                #print('end: ', actEnd)
                #print(startEnd)
                #print('remaining events to plan: ', nonScheduled)
                #add to list of event times
                periodStart= actEnd           
                actInPeriod=int((periodEnd-periodStart)/self.duration)
            
        
        #for event in self.eventTimes:
            #print(event)

    def get_event_time(day):
        return self.eventTimes[day]
    
class ClassList():
    def __init__(self, studentFile):
        #add number of days in week
        #start and stop times
        self.studentList=[]
        self.readingGroupList=[]
        
        studentData= self.read_stu_file(studentFile)
        
        #make list of of all students
        for kid in studentData:
            self.studentList.append(Student(kid))
       
        #count how many reading groups/levels and make list of group numbers
        maxGroupNum=0 
        for student in self.studentList:        
            if student.groupNumber > maxGroupNum:
                maxGroupNum= student.groupNumber
        #print('max group number', maxGroupNum)

        #initialize reading group for each level
        for i in range(0, maxGroupNum+1):
            self.readingGroupList.append(Reading_Group(i))

        #add each student to reading list
        for student in self.studentList:
            self.readingGroupList[student.groupNumber].add_student_to_group(student)

        #test print students in each reading group
        #for group in self.readingGroupList:
            #group.print_reading_group()    

    def read_stu_file(self, filePath):
    #input: filepath to student csv file
    #output: list of students, each student is list of frist, last and reading group/level 
    #reading group number/level must start at 0 and be contiguous to highest group number
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

class Student():
    def __init__(self, studentData):
        self.first= studentData[0]
        self.last= studentData[1]
        self.readingLevel= int(studentData[2])
        self.groupNumber= int(studentData[2])

        self.activityList= [] 

    def print_student(self):
        print('{} {} {} {} {}'.format('student: ', self.first, self.last, 'reading level: ', self.readingLevel))


class Reading_Group():   
    def __init__(self, groupNumber):
        self.groupNumber= groupNumber
        self.studentList=[]
        self.activityList=[]

    def add_student_to_group(self, student):
        self.studentList.append(student)    
    
    def print_reading_group(self):
        print('Reading Group ', self.groupNumber)
        print('Student List:')
        if self.studentList:
            for student in self.studentList:
                student.print_student()
        else:
            print('no students in group')

class Staff_Schedule():
    def __init__(self):
        self.dayCount=0
        self.maxTimesInOut=0
        self.teacherList=[]

    def read_teachers(self, filePath):
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
        
    #add pattern matching to identify how many in/out times for eac day
    def teacher_sched(self, teacherTimes):
        #input: list of strings each string lis line from teacher schedule file
        #output list of teacher objects
        #start by just making general schedule for one day/all week
        teacherList=[]
        #print('teacherTimes list')
        #print(teacherTimes)
        #orgainize teacher schedule by teacher or day?  teacher
        #count how many days in schedule and how many in/out times in day from file
        #need to have class set up before this point
        
        #hard coded, need to add functions
        self.dayCount=4
        self.maxTimesInOut=2
        dayCount=self.dayCount
        inOutCount=self.maxTimesInOut

        for line in teacherTimes:
            #list of days, each day is list of in/out lists
            dayList=[]
            name =line.pop(0)
            #list of days, each day is list of time chunks which is list  clockin/out times

            #loop for each day
            for i in range(0, dayCount):
                #each day is list of in/out times
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

            #change to separate function
            #print(name)
            #print each day
            #for i in range(0, dayCount): 
                #print('day', i)
                #for j in range(0, inOutCount):
                #for j in range(0, len(dayList[i])):
                    #if(dayList[i][j]):
                        #print('In: ', dayList[i][j][0])
                        #print('Out: ', dayList[i][j][1])
          
            self.teacherList.append(Teacher(name, dayList))
        return
        
    def print_staff(self):
       print('print staff function')
       for teacher in self.teacherList:
            teacher.print_teacher()
            
class Teacher():
    def __init__(self, name, schedule):
       self.name=name
       self.schedule=schedule
    
    def print_teacher(self):
        print(self.name)
        day=0
        for i in self.schedule:
            print('day ', day)
            inOut= 0
            for time in self.schedule[day]:
                if self.schedule[day][inOut]:
                    print(self.schedule[day][inOut][0])
                    print(self.schedule[day][inOut][1])
                inOut= inOut + 1
            day=day + 1

    def get_days_inOuts(self, day):
        return self.schedule[day]

#class ReadingActivity(filePath):
    #pass
    


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

#.........................................
#turn times from 12 to 24 then to decimal
#.........................................

#time_to_min('12:30:00 PM')
#time_to_min('9:30 AM')
#time_to_min('10:30')
#time_to_min('2:30')
#min_to_time(750)
#min_to_time(570)
#min_to_time(630)
#min_to_time(870)

# .............................
# make class schedule parameteres
# .............................
# need to add a bit of error handling for bad input

numberOfDays=4
actPerDay=4
start1=0
end1=40
start2=60
end2=100
actDuration=20
schedParams1= Schedule_Parameters(numberOfDays, actPerDay, actDuration, start1, end1, start2, end2)

# ......................
# test student class 
# ......................

#input list[0] joe then student1.first == 'joe'
testStData=['joe', 'smith', 1]
student1= Student(testStData)
#student1.print_student()


#...............................
# make classList of students
#...............................

#csv <name>,<last>,<number> then list[1] == <last>
filePath='students.csv'
myClassList= ClassList(filePath)


# .................................
# make teacher clas and schedule
# .................................

teacherSchedLines=[]
myStaff =Staff_Schedule()
teacherSchedLines= myStaff.read_teachers('teacher.csv')
myStaff.teacher_sched(teacherSchedLines)
#myStaff.print_staff()



#test with extra padding
numberOfDays=4
actPerDay=4
start1=0
end1=50
start2=60
end2=115
actDuration=20
schedParams2= Schedule_Parameters(numberOfDays, actPerDay, actDuration, start1, end1, start2, end2)

#test with less parameters
numberOfDays=4
start1=0
end1=0
actDuration=20
schedParams3= Schedule_Parameters(numberOfDays, actPerDay, actDuration, start1, end1)


# .............................
# put it all together!!???
# .............................
myClassSched=Class_Schedule(myStaff, myClassList, schedParams1)
myClassSched.make_reading_lessons()
