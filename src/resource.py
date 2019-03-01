class Resource():
    def __init__(self, name, number, start, end, freq):
        self.name= name
        self.number= number
        self.start= start
        self.end= end
        self.freq= freq
        self.eventList=[]
    
    def print_resource(self):
        print('Name:', self.name)
        print('Number Available:', self.number)
        print('Start:', self.start)
        print('End:', self.end)
        print('Frequency of Use:', self.freq)


class Resource_Sched():
    def __init__(self):
        self.resources={}
        self.resourceList=[]

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
        count=0 

        for name in self.resourceList: 
            for day in range(0, numberOfDays):
                for timeBlock in dailyEvents[day]:
                    if timeBlock[0] >= self.resources[name].start and timeBlock[1]<= self.resources[name].end:
                        for i in range(0, self.resources[name].number):

                            #make event
                            newEvent= readingGroups.Event(day, timeBlock[0], timeBlock[1], self.resources[name].name)
                            newEvent.num=count
                            count=count+1
                            
                            #add event to list or dictionary
                            self.resources[name].eventList.append(newEvent)


import readingGroups
import timeConvert as tm
