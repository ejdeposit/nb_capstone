#Evan DePosit
#New Beginnings
#capstone
#This file contains class data structures to store student information and functions to read that information from a file

# ----------------------------------------------------------------------------------------------------------------------------------
#                                                       $match
# ----------------------------------------------------------------------------------------------------------------------------------

class Graph():
    def __init__(self):
        self.queue=[]
        self.U=None
        self.V=None
        self.E=None
        self.unionVU=[]

        #for vertex in U:
            #self.unionVU.insert(vertex.num, vertex)    

        #for vertex in V:
            #self.unionVU.insert(vertex.num, vertex)    
    

    def print_matches(self):
        print('vetex->mate')
        for vertex in self.unionVU:
            if (vertex.mate):
                print('{} {} {} {} {}'.format('v', vertex.num, '->', vertex.mate.num, '  '))
            else:
                print('{} {} {} {} {}'.format('v', vertex.num, '->', 'N', '  '))
        print('')

    def print_queue(self):
        print('queue: ', end='') 
        for v in self.queue:
            v.print_vertex()
        print('')

    def print_set(self, part):
        print('set ', end='') 
        for v in part:
            v.print_vertex()
        print('')
    
    def init_queue(self):
        self.queue=[]
        for vertex in self.V:
            if vertex.mate is None:
                self.queue.append(vertex)

    def remove_labels(self):
        for vertex in self.V:
            vertex.label=None
        for vertex in self.U:
            vertex.label=None

    def print_debug(self, loc):
        print('{} {}'.format(loc, 'vetex->mate'))
        for vertex in self.unionVU:
            if (vertex.mate):
                print('{} {} {} {}'.format(vertex.num, '->', vertex.mate.num, '  '))
            else:
                print('{} {} {} {}'.format(vertex.num, '->', 'N', '  '))
        print('')

    def max_match(self):
    # Maximum Matching in Bipartite Graph Algorithm
    # the purpose of this function is to match up teachers with reading groups.
    # another function will generate edges based on times the teacher is available
    #and which reading levels they can work with
        self.init_queue()
        while self.queue:
            w= self.queue.pop(0)
            #change to my own search function if time
            if w in self.V:
                for u in self.E[w.num]:
                    #if u is free in list of vertices connected to w
                    if u.mate is None:
                        w.mate=u
                        u.mate=w
                        #following labeling, umatching, etc will take place after finding last free 
                        v=w
                        while(v.label is not None):
                            u=v.label
                            if((u.mate == v) and (v.mate== u)):
                                v.mate=None
                                u.mate=None
                            v=u.label
                            v.mate=u
                            u.mate=v
                        self.remove_labels()
                        self.init_queue()
                        #break from for loop because at end of traversal
                        break
                    else:
                        if((w.mate != u) and (u.mate != w) and (u.label is None)):
                            u.label= w
                            self.queue.append(u)
            #else: w in U and matched
            else:
                #label the mate v of w with "w"
                w.mate.label= w                            
                #enqueue(Q, v) v as in mate v of w?
                self.queue.append(w.mate)
        return


    def foo(self):
        print('foo')


# ----------------------------------------------------------------------------------------------------------------------
#                                                           $act $event $vertex
# ---------------------------------------------------------------------------------------------------------------------

class Vertex(): 
#vertex will be parent class of reading activities and scheduled events classes
    def __init__(self):
        self.num=None 
        self.label=None 
        self.mate=None       

    def print_vertex(self):
        print(self.num, end=' ')



#classes
class Activity(Vertex):
    def __init__(self, actType):
        super().__init__()
        self.type=actType
        eventTime=None

class Reading_Group_Activity(Activity):
    def __init__(self, group, day, actType):
        super().__init__(actType)
        self.readingGroup= group  
        self.readingLevel=None
        self.day=day
        
       # self.groupNumber= groupNumber
       # self.studentList=[]
       # self.activityList=[]

    def print_act(self):
        print('Group: ', self.readingGroup.groupNumber)
        print('Day: ', self.day)
        print('Activity Type: ', self.type)
        #if self.num:
        #    print('vertex number: ', self.num)
        print('vertex number: ', self.num)
    
class Event(Vertex):
    def __init__(self, day, start, end, eventType, teacher=None):
        super().__init__()
        self.day= day
        self.start=start
        self.end= end
        self.teacher=teacher 
        #can be either pointer to one student or group of students
        self.type=eventType
        self.students=None

    def print_event(self):
        print()
        print('Event: ', self.type)
        if self.teacher:
            print('Teacher: ', self.teacher.name)
        print('day: ', self.day)
        print('Start: ', min_to_time(self.start), 'End: ', min_to_time(self.end))
        if self.num:
            print('vertex number: ', self.num)


# ----------------------------------------------------------------------------------------------------------------------
#                                                           $sched
# ---------------------------------------------------------------------------------------------------------------------

class Reading_Group_Sched(Graph):
    def __init__(self, teacherSchedule, classList, scheduleTimes):
        super().__init__()
        self.teacherSchedule=teacherSchedule
        self.classList=classList
        #schedule times is schedule_parameters object
        self.schedParams=scheduleTimes  
        #dictionary key= day, item list of events on that day
        self.eventSched={}
        #dictionary key= day, item list of activities of all groups
        self.actSched={}

    def print_group_teacher(self):
        weekLen= self.schedParams.days

        for groupNumber in self.classList.groupNumberList:
            self.classList.readingGroups[groupNumber]
            print('Group', self.classList.readingGroups[groupNumber].groupNumber, 'Activity Event Match')
            for act in self.classList.readingGroups[groupNumber].activityList:
                act.print_act()
                print()
                if act.mate:
                    act.mate.print_event()
                else:
                    print('NO MATCH')
                print()
                print()
            print()
            print()
            print()

    def make_group_event(self):
        """
        input:self used to access teacher objects
        output: creates event, adds it to list for teachers and master events list
        """
        weekLen= self.schedParams.days
        allEvents=[]

        #interate through teachers
        for teacher in self.teacherSchedule.teacherList:        
            #print(teacher.name)

            #iterate through each day in teachers schedule
            for day in range(0, weekLen):    
                
                teacherDayEventList=[]

                #get event times for that day from parameters object
                #get in/out times for that day from teacher class
                eventTimes= self.schedParams.get_days_eTime(day)               
                teacherTimes= teacher.get_days_inOuts(day)
                                
                # test print e times and teacher times to see if they line up
                #self.schedParams.print_days_eTimes(day) 
                #print('day ', day, 'teacher availability')
                #print(teacherTimes)

                #interate over list of inout times` and comapre to event times for each day
                for event in eventTimes:
                    for inOut in teacherTimes:
                        #if list is not empty
                        #compare if in time is less than or equal to event start 
                        #and out time is greater than or equal to event end time
                        if inOut and inOut[0] <= event[0] and inOut[1]>= event[1]:
                            #create event make_event(day, start, stop, teacher)
                            newEvent= Event(day, event[0], event[1], "Small Group Lesson", teacher)
                            
                            teacherDayEventList.append(newEvent)       

                            #add to master list doesn't have to be function can just append it to 
                            allEvents.append(newEvent)                            
                            #newEvent.print_event()
                            
                #add to teachers list
                teacher.add_event(teacherDayEventList, day)

        #allEvents not organized by day need separate function
        #self.groupEventList= allEvents                            
        self.add_events(allEvents)
        self.V= allEvents
        

    def add_events(self, eventList):
    #input: list of events
    #output: dictionary of events by day
    #function interates through list of events makes list for each day, list is not organized, just for max match
        for event in eventList:
            if event.day in self.eventSched:
                self.eventSched[event.day].append(event)
            else:
                self.eventSched[event.day]= []
                self.eventSched[event.day].append(event)
             
    #generate activity list for each readingGroup 
    def make_group_act(self):
        weekLen= self.schedParams.days
        classActList=[]

        for groupNumber in self.classList.groupNumberList:
            groupActList=[]

            for day in range(0, weekLen):
                #reading_group_Act(self, group, day, actType):
                newAct= Reading_Group_Activity(self.classList.readingGroups[groupNumber], day, 'Small Group Lesson')
                #newAct.print_act()         
                #add each act to groups list and sched act list for maxMatch
                groupActList.append(newAct)
                classActList.append(newAct)

            #add group act list to group class object. in group function add it to each stuent too
            self.classList.readingGroups[groupNumber].add_actList(groupActList)  
       
        #add group act list to class schedule (dictionary day:actList) if keeping as a list instead of dictionary by day 
        self.add_act_list(classActList)
        
        #add group act to set u in graph class
        self.U= classActList 
        
        #print('U in make grup act funct')
        #self.print_set(self.U) 
        #self.print_act_list(self.U)
        
    def print_act_list(self, actList):
        print('print act list')
        for act in actList:
            act.print_act()


    def add_act_list(self, classActList):
    #input: unordered list of all activities created for every group
    #output: add activities to Reading Group sched.actSched by day
        for activity in classActList:
            if activity.day in self.actSched:
                self.actSched[activity.day].append(activity)
            else:
                self.actSched[activity.day]=[]
                self.actSched[activity.day].append(activity)

    def add_teacher_pref(self):
        str1= 'For each staff member, enter the group number of each group that may be scheduled with the staff member'
        str2= 'separating each group number with a spae and entering return when finished'
        str3= 'If all groups may be scheduled with the staff member, enter all'
        
        GroupsNumbers=[]
        
        print('{} {} {}'.format(str1, str2, str3))

        for teacher in self.teacherSchedule.teacherList:

            #remove break when finished testing
            break

            groupPref=[]
            
            line=input(teacher.name +': ')
            if 'all' in line or 'All' in line:
                #add group pref to teacher
                allGroups= self.classList.numOfGroups
                for i in range(1, allGroups+1):
                    groupPref.append(i)
            else:
                numList=line.split(' ')
                for numStr in numList:
                    isNumber= re.match('^\d+$', numStr)
                    if isNumber:
                        num= int(numStr)
                        groupPref.append(num) 
                #add group pef to teacher     
            teacher.groupPref=groupPref    
            print(groupPref)
            
        #hard code teacher pref for repeated testing
        self.teacherSchedule.teacherList[0].groupPref= [1,2,3]
        self.teacherSchedule.teacherList[1].groupPref= [1,2,3]
        self.teacherSchedule.teacherList[2].groupPref= [3]
        
        #for teacher in self.teacherSchedule.teacherList:
            #print(teacher.name, teacher.groupPref)


    def set_edges(self):
        vertexCount=0
        weekLen=self.schedParams.days
        edgeList={}

        #number vertexes
        for i in range(0, weekLen):
            for event in self.eventSched[i]:
                event.num=vertexCount      
                vertexCount= vertexCount+1
                
        for i in range(0, weekLen):
            for act in self.actSched[i]:
                act.num=vertexCount      
                vertexCount= vertexCount+1
       
        for teacher in self.teacherSchedule.teacherList:
            pref= teacher.groupPref
            for day in range(0, weekLen):
                for event in teacher.lessonEventSched[day]:
                    for act in self.actSched[day]:
                        if act.readingGroup.groupNumber in pref:
                            if act.num in edgeList:
                                edgeList[act.num].append(event)
                            else:
                                edgeList[act.num]=[]
                                edgeList[act.num].append(event)
                            if event.num in edgeList:
                                edgeList[event.num].append(act)
                            else:
                                edgeList[event.num]=[]
                                edgeList[event.num].append(act)

                            #print('match')
                            #act.print_act()
                            #event.print_event()
                            #print()
            self.E=edgeList                    
                            
class Schedule_Parameters():
    #def __init__(self, days, actPerDay, duration, start1, end1, start2=None, end2=None):
    def __init__(self, days, actPerDay, duration):
        self.days=days
        self.actPerDay=actPerDay
        self.duration = duration
        #list of of days, each day is  list of start and stop times
        self.dailyEvents=[]

    def week_len(self):
        return self.days

    def set_weeks_eTimes(self, startEndList):
        #input: list of start and end times for each day of the week
        #output: list of event times for each day
        for times in startEndList:
            start1 = times[0]
            end1 = times[1]
            if len(times) > 2:
                start2= times[2]
                end2= times[3]
            else:
               start2=None
               end2 =None
            daysEvents=[]
            daysEvents= self.set_days_eTimes(start1, end1, start2, end2)
            self.dailyEvents.append(daysEvents)  

    def set_days_eTimes(self, start1, end1, start2, end2):
        daysEvents=[]
        event=0
        periodStart=start1
        periodEnd=end1
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

            daysEvents.append(startEnd)

            #update variables for next time through loop
            nonScheduled=nonScheduled-1
            #print('start: ', actStart)
            #print('end: ', actEnd)
            #print(startEnd)
            #print('remaining events to plan: ', nonScheduled)
            #add to list of event times
            periodStart= actEnd           
            actInPeriod=int((periodEnd-periodStart)/self.duration)
             
        if(nonScheduled and start2):
            periodStart=start2
            periodEnd=end2
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
                daysEvents.append(startEnd)
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
        return daysEvents
        
    def print_days_eTimes(self, day):
        """
        input: day that exist in list of events times for each day in schedule
        output: void, prints list of events on that day
        """
        print('day', day, 'event times')
        if(self.dailyEvents[day]):
            print(self.dailyEvents[day])
        else:
            print('list empty')

    def print_all_eTimes(self):
        print('All events times for week')
        print(self.dailyEvents)
        
    def get_days_eTime(self, day):
        """
        input day 
        output list of n elements, each element is list of start and stop time of that  event  
        """
        return self.dailyEvents[day]

def min_to_time(minTime):

    minutes=minTime%60
    hour=int(minTime/60)
    #print('hour= ', hour)
    #print('minutes= ', minutes)
    
    if hour == 12:
        timeOfDay='PM'
    elif hour > 12:
        timeOfDay='PM'
        hour= hour-12
    else:
        timeOfDay='AM'    
    
    time=str(hour) + ':' + str(minutes) + ' ' + timeOfDay
    #print('time= ', time)
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

# -------------------------------------------------------------------------------------------------------------------
#                                                      $student
# -----------------------------------------------------------------------------------------------------------------

class Class_List():
    def __init__(self, studentFile):
        #add number of days in week
        #start and stop times
        self.studentList=[]
        #self.readingGroupList=[]
        #delete this
        self.numOfGroups=0
        self.groupNumberList=[] 
        self.readingGroups= {}

        studentData= self.read_stu_file(studentFile)
        
        #make list of of all students
        for kid in studentData:
            self.studentList.append(Student(kid))
        
        
        #count how many reading groups/levels and make list of group numbers
        #or make list of readingGroups an make dictionary for readingGroups
        maxGroupNum=0 
        for student in self.studentList:        
            if student.groupNumber > maxGroupNum:
                maxGroupNum= student.groupNumber
        self.numOfGroups=maxGroupNum
        #delete above -----------------------------------------------------------------------

        #make list of student groups to allow iterating through groups in dictionary
        groupNumberList=[]
        for student in self.studentList:
            if student.groupNumber not in groupNumberList:
                groupNumberList.append(student.groupNumber)
        self.groupNumberList=groupNumberList

        #make dictionary of student groups
        for student in self.studentList:
            if student.groupNumber in self.readingGroups:
                self.readingGroups[student.groupNumber].add_student_to_group(student)
            else:
                self.readingGroups[student.groupNumber]=Reading_Group(student.groupNumber)
                self.readingGroups[student.groupNumber].add_student_to_group(student)
                
        #test print students in each reading group
        #for group in self.groupNumberList:
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

    def make_free_list(self, eventTimes, weekLen):
        for student in self.studentList:
            student.make_free_list(eventTimes, weekLen)

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

    def add_actList(self, groupActList):
        #input list of readingGroup activities for group
        #output add list to groups act list and to each students sched
        self.activityList=groupActList
       
        for student in self.studentList: 
            student.add_group_act(groupActList)


class Student():
    def __init__(self, studentData):
        self.first= studentData[0]
        self.last= studentData[1]
        self.readingLevel= int(studentData[2])
        self.groupNumber= int(studentData[2])
        self.actSched={} 
        self.eventSched={} 
        self.freeList={}
        
    def add_group_act(self, groupActList):
        for activity in groupActList:
            if activity.day in self.actSched:
                self.actSched[activity.day].append(activity)
            else:
                self.actSched[activity.day]=[]
                self.actSched[activity.day].append(activity)

    def print_student(self):
        print('{} {} {} {} {}'.format('student: ', self.first, self.last, 'reading level: ', self.readingLevel))

    def make_free_list(self, eventTimes, weekLen):

        for day in range(0, weekLen):
            dayFreeList=[]
            #needs to have conditional if no events scheduled
            #print(self.eventSched[day])

            #if no events planned on day
            if day not in self.eventSched:
                for startEnd in eventTimes:
                    newFreeEvent= Event(day, startEnd[0], startEnd[1], 'Free List Event')
                    dayFreeList.append(newFreeEvent)
                #add freelist to hash table for specified day 
                self.freeList[day]=dayFreeList 
            
            else:
                for startEnd in eventTimes:
                    noEvent=True
                    for event in self.eventSched[day]:
                        if event.start == startEnd[0]:
                            noEvent=False
                    if noEvent:
                        newFreeEvent= Event(day, startEnd[0], startEnd[1], 'Free List Event')
                        dayFreeList.append(newFreeEvent)
                #add to freelist for to day to hash table
                self.freeList[day]=dayFreeList 
   
    def print_freeList(self, day, weekLen):
        #print('Day', day, 'Free List: ')
        if day in freeList:
            for event in freeList[day]:
                event.print_event()
        else:
            print('No Free List Events')
#-------------------------------------------------------------------------------------------------------------------------------    
#                                                         $teacher
# -----------------------------------------------------------------------------------------------------------------------------             

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
          
            self.teacherList.append(Teacher(name, dayList, dayCount))
        return
        
    def print_staff(self):
        print('print staff function')
        for teacher in self.teacherList:
            teacher.print_teacher()
            

class Teacher():
    def __init__(self, name, schedule, weekLen):
        self.name=name
        self.schedule=schedule
        #dictionary is schedule with day as key and list of lesson events as item
        self.lessonEventSched={}
        self.groupPref=[]
    
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

    def add_event(self, eventList, day):
        self.lessonEventSched[day]=eventList    
         
# ---------------------------------------------------------------------------------------------------------------------------
#                                                                   $main
# ---------------------------------------------------------------------------------------------------------------------------


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
actDuration=20
schedParams1= Schedule_Parameters(numberOfDays, actPerDay, actDuration)

#set set weeks eTimes
weekTimes=[]

for i in range(0, 4):
    start1=time_to_min('11:15')
    end1=time_to_min('11:55')
    start2=time_to_min('12:40')
    end2=time_to_min('1:20')
    dayTimes=[]
    dayTimes.append(start1)
    dayTimes.append(end1)
    dayTimes.append(start2)
    dayTimes.append(end2)
    weekTimes.append(dayTimes)

#test with extra padding
#test with less parameters
#start1=time_to_min('11:15')
#end1=time_to_min('11:55')
#dayTimes=[]
#dayTimes.append(start1)
#dayTimes.append(end1)
#weekTimes.append(dayTimes)

schedParams1.set_weeks_eTimes(weekTimes)
#schedParams1.print_all_eTimes()

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
myClassList= Class_List(filePath)

# .................................
# make teacher clas and schedule
# .................................

teacherSchedLines=[]
myStaff =Staff_Schedule()
teacherSchedLines= myStaff.read_teachers('teacher2.csv')
myStaff.teacher_sched(teacherSchedLines)

#myStaff.print_staff()


# .............................
# put it all together!!???
# .............................
readingGroupSched1=Reading_Group_Sched(myStaff, myClassList, schedParams1)
readingGroupSched1.make_group_event()
readingGroupSched1.make_group_act()
readingGroupSched1.add_teacher_pref()
readingGroupSched1.set_edges()

readingGroupSched1.unionVU= readingGroupSched1.V + readingGroupSched1.U



#why are none objects appearing in vertex list?
readingGroupSched1.max_match()
readingGroupSched1.print_group_teacher()

readingGroupSched1.print_matches()

# .............................
#          make free list
# .............................
#print(schedParams1.dailyEvents)
myClassList.make_free_list(schedParams1.dailyEvents, numberOfDays)

