class Resource():
    def __init__(self, name, number, start, end):
        self.name= name
        self.number= number
        self.start= start
        self.end= end
        self.freq= freq

def make_resources():
    str1= "enter the number of different types of resources used for individual reading activities"
    resources={} 
    resourceTypeList=[] 
    resourceNum =input(str1 + ': ')

    for i in range(0, resourceNum):
        print('resource ', i, ':', sep='')
        name= input('Name: ')
        number= input('Number available: ')
        start= input('Starting time of availability: ')
        end= input('Ending time of availability: ')
        freq= input('How often should each student use the resource: ')  
          
        resourceTypeList.append(name) 
        resources.[name]=Resource(name, number, start, end, freq)

def make_resource_events(resources, resourceTypeList)
    pass

import readingGroups

make_resources()
