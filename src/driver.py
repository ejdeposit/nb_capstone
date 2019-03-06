#Evan DePosit
#New Beginnings
#capstone
#This file contains class data structures to store student information and functions to read that information from a file

# ---------------------------------------------------------------------------------------------------------------------------
#                                                                   $main
# ---------------------------------------------------------------------------------------------------------------------------

import readingGroups as rg
import timeConvert as tm
import resource as rs
import student as st

#.........................................
#turn times from 12 to 24 then to decimal
#.........................................

#tm.tm_to_min('12:30:00 PM')
#tm.time_to_min('9:30 AM')
#tm.time_to_min('10:30')
#tm.time_to_min('2:30')
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
schedParams1= rg.Schedule_Parameters(numberOfDays, actPerDay, actDuration)

#set set weeks eTimes
weekTimes=[]

for i in range(0, 4):
    start1=tm.time_to_min('11:15')
    end1=tm.time_to_min('11:55')
    start2=tm.time_to_min('12:40')
    end2=tm.time_to_min('1:20')
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
student1= st.Student(testStData)
#student1.print_student()


#...............................
# make classList of students
#...............................

#csv <name>,<last>,<number> then list[1] == <last>
filePath='students.csv'
myClassList= st.Class_List(filePath)

# .................................
# make teacher clas and schedule
# .................................

teacherSchedLines=[]
myStaff = rg.Staff_Schedule()
teacherSchedLines= myStaff.read_teachers('teacher2.csv')
myStaff.teacher_sched(teacherSchedLines)

#myStaff.print_staff()


# .............................
# put it all together!!???
# .............................
readingGroupSched1= rg.Reading_Group_Sched(myStaff, myClassList, schedParams1)
readingGroupSched1.make_group_event()
readingGroupSched1.make_group_act()
readingGroupSched1.add_teacher_pref()
readingGroupSched1.set_edges()
readingGroupSched1.unionVU= readingGroupSched1.V + readingGroupSched1.U
readingGroupSched1.max_match()
#test print of matches
#readingGroupSched1.print_group_teacher()
#readingGroupSched1.print_matches()

# .............................
#          make free list
# .............................
#print(schedParams1.dailyEvents)

#adds reading group events to students schedule
myClassList.sched_readingGroups(numberOfDays)

# filles in empty slots with free events
myClassList.make_free_list(schedParams1.dailyEvents, numberOfDays)

#test print student scheudle and free list 
#make funct to print both freeList sched for each student in class list
#make func to print freelist for student
#make func to print sched for student
#make separate funct to print both individually for classList
myClassList.print_freeList_sched(numberOfDays)

# .............................
#          $resource schedule
# .............................
resourceSched1= rs.Resource_Sched(myClassList)

resourceSched1.make_resources()
#resourceSched1.print_all_resources()

resourceSched1.make_resource_events(schedParams1.dailyEvents, numberOfDays)

resourceSched1.init_resource_use()
resourceSched1.set_edges()
resourceSched1.match_events()
myClassList.print_sched(numberOfDays)

# .............................
#          $print sched
# .............................
