class Resource():
    def __init__(self, name, number, start, end, freq):
        self.name= name
        self.number= number
        self.start= start
        self.end= end
        self.freq= freq
        self.eventList=[]
        self.eventSched={}
        self.eventCount=None

    def print_resource(self):
        print('Name:', self.name)
        print('Number Available:', self.number)
        print('Start:', self.start)
        print('End:', self.end)
        print('Frequency of Use:', self.freq)


class Resource_Sched():
    def __init__(self, classList):
        self.resourceList=[]
        self.resources={}
        self.classList=classList 
        self.masterResourceEventList=[]
        self.masterFreeEventList=[]
        self.masterEventSched={}
        self.weekLen=None 
        self.resourceUse={}

    def make_resources(self):
        resources={} 
        resourceList=[] 
        
        name='ipad'
        resources[name]=Resource(name, 30, 675, 800, 1)
        resourceList.append(name) 

        name='read to self'
        resources[name]=Resource(name, 30, 675, 800, 1)
        resourceList.append(name) 
       
        name='partner reading'
        resources[name]=Resource(name, 30, 675, 800, 1)
        resourceList.append(name) 

        name='writing about reading'
        resources[name]=Resource(name, 30, 695, 800, 1)
        resourceList.append(name) 

        name='listening'
        resources[name]=Resource(name, 5, 675, 800, 1)
        resourceList.append(name) 
        
        self.resources=resources
        self.resourceList=resourceList
    #make_resources
    def foo(self):
        str1= "enter the number of different types of resources used for individual reading activities"
        resources={} 
        resourceList=[] 
        resourceNum =input(str1 + ': ')
        resourceNum= int(resourceNum) 

        for i in range(0, resourceNum):
            print('resource ', i, ':', sep='')
            name= input('Name: ')
            name = name.lower()
            number= input('Number available: ')
            start= input('Starting time of availability: ')
            start= tm.time_to_min(start)
            end= input('Ending time of availability: ')
            end= tm.time_to_min(end)
            freq= input('How often should each student use the resource: ')  
              
            resourceList.append(name) 
            resources[name]=Resource(name, number, start, end, freq)

        self.resources=resources
        self.resourceList=resourceList


    def print_all_resources(self):
        print()
        for name in self.resourceList:
            self.resources[name].print_resource() 
            print()

    def make_resource_events(self, dailyEvents, numberOfDays):
        self.weekLen=numberOfDays
        for name in self.resourceList: 
            count=0 
            for day in range(0, numberOfDays):
                for timeBlock in dailyEvents[day]:
                    if timeBlock[0] >= self.resources[name].start and timeBlock[1]<= self.resources[name].end:
                        for i in range(0, self.resources[name].number):

                            #make event
                            newEvent= readingGroups.Event(day, timeBlock[0], timeBlock[1], self.resources[name].name)
                            newEvent.num=count
                            count=count+1
                            
                            #add event to list for resource  
                            self.resources[name].eventList.append(newEvent)
                            #add event to resource's sched by day
                            if day in self.resources[name].eventSched:
                                self.resources[name].eventSched[day].append(newEvent)

                            else:
                                self.resources[name].eventSched[day]=[]
                                self.resources[name].eventSched[day].append(newEvent)

                            #add event to list for resource_sched 
                            self.masterResourceEventList.append(newEvent)
                            #add event to resource_sched event sched by day
                            if day in self.masterEventSched:
                                self.masterEventSched[day].append(newEvent)
                            else:
                                self.masterEventSched[day]=[]
                                self.masterEventSched[day].append(newEvent)
            self.resources[name].eventCount=count

    def number_vertices(self, vertexList):
        count=0
        for vertex in vertexList:
            vertex.num=count
            count+=1

    def set_edges(self):
    #there is no point to edge list 
        weekLen=self.weekLen
        studentList=self.classList.studentList
        edgeList={}
        studentFreeEvents=[]
        allEvents=[]

        for student in studentList:
            for i in range(0, weekLen):
                if i in student.freeList:
                    for freeEvent in student.freeList[i]:
                        studentFreeEvents.append(freeEvent)

        self.masterFreeEventList=studentFreeEvents
        allEvents= studentFreeEvents + self.masterResourceEventList
       
        #print(len(studentFreeEvents))
        #print(len(allEvents))
        self.number_vertices(allEvents)
       
        #connect students' freeEvents to resourceEvents based on time
        for freeEvent in studentFreeEvents:
            #interate through resources
            for resourceName in self.resourceList:
                #iterate events on  resources sched for secified day
                for resourceEvent in self.resources[resourceName].eventSched[freeEvent.day]:
                    #if resource event is same time free event add to dictionary of edges
                    #print('.', sep='', end='')
                    if resourceEvent.start == freeEvent.start:
                        if freeEvent.num in edgeList:
                            edgeList[freeEvent.num].append(resourceEvent.num)
                        else:
                            edgeList[freeEvent.num]=[]
                            edgeList[freeEvent.num].append(resourceEvent.num)
                        if resourceEvent.num in edgeList:
                            edgeList[resourceEvent.num]=freeEvent.num
                        else:
                            edgeList[resourceEvent.num]=[]
                            edgeList[resourceEvent.num]=freeEvent.num
    
    def init_resource_use(self):
        #2-d dictionary first key is student name, second key is resource name
        resourceNum={}
        for student in self.classList.studentList:
            resourceNum[student.fullName]={}
            for resourceName in self.resourceList:
                resourceNum[student.fullName][resourceName]=0
        self.resourceUse=resourceNum
        

    def match_events(self):

        studentFreeList=set(self.masterFreeEventList)
        #resourceEventList=set(self.masterResourceEventList) 

        totalEvents={}
        
        #copy event count of each resourced to dictionary name:eventCount
        for resourceName in self.resourceList:
            totalEvents[resourceName]=self.resources[resourceName].eventCount

        while studentFreeList:

            minWeight=999999999
            freeEvent=studentFreeEvents.pop()
            studentName=freeEvent.fullName
            day=freeEvent.day

            #find resourceEvent at same time with lowest weight
            for resourceEvent in self.eventSched[day]:
                resourceName= resourceEvent.type
                if resourceEvent.day ==  day and resourceEvent.mate==None and resourceEvent.start == freeEvent.start: 

                    #need to make sure student full name is attached to freeEvent
                    #need to make sure resource name is attache to resource event
                    ammHeld=self.resourceUse[studentName][resourceName]
                    ammCirc=self.resources[resourceName]
                    edgeWeight=((100 * ammHeld)/ ammCirc) < minWeight

                    if edgeWeight < minWeight:
                        minWeight = edgeWeight    
                        resourceMatch=resourceEvent
            
            studentFreeList.remove(resourceMatch)
            #match togheter vertices, not totally necessary yet
            resourceMatch.mate= freeEvent 
            freeEvent.mate= resourceMatch 
            #add event to student schedule
            student=freeEvent.students
            student.eventSched[day].append(resourceMatch)
            #min is found, update resourceuse table for student
            resourceName=resourceMatch.type
            self.resourceUse[studentName][resourceName]+=1

import readingGroups
import timeConvert as tm
