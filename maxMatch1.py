#Evan DePosit
#New Beginnings
#capstone project
#This file contains functions for maximum mathing in bipartite graphs algorithms to match teachers to reading groups

#graph clas will be parent class of classroom list class
class graph():
    def __init__(self, V, U, E):
        self.queue=[]
        self.U=U
        self.V=V
        self.E=E
        self.unionVU=[]

        for vertex in U:
            self.unionVU.insert(vertex.num, vertex)    

        for vertex in V:
            self.unionVU.insert(vertex.num, vertex)    

    def print_matches(self):
        for vertex in self.unionVU:
            if (vertex.mate):
                print('{} {} {} {}'.format('vertex ', vertex.num, 'match = ', vertex.mate.num))
            else:
                print('{} {} {} {}'.format('vertex ', vertex.num, 'match = ', 'none'))

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
        pass


    def max_match(self):
    # Maximum Matching in Bipartite Graph Algorithm
    # the purpose of this function is to match up teachers with reading groups.
    # another function will generate edges based on times the teacher is available
    #and which reading levels they can work with
        self.init_queue()
        while self.queue:
            w= self.queue.pop(0)
            if w in self.V:
                for u in self.E[w.num]:
                    #if u is free
                    if u.mate is None:
                        #DEBUG
                        print('if u.mate free before match')
                        self.print_matches()
                        #DEBug
                        w.mate=u
                        u.mate=w

                        print('if u.mate free after match')
                        self.print_matches()
                        #following labeling, umatching, etc will take place after finding last free 
                        v=w
                        while(v.label):
                            u=v.label
                            v.mate=None
                            u.mate=None
                            print('while loop before match')
                            self.print_matches()
                            v=u.label
                            v.mate=u
                            u.mate=v
                            print('while loop after match')
                            self.print_matches()
                            #DEBUG: need to find out why two vertices missing match,
                            #even though their match partner has them matched
                            #print('after matching')
                            #print(str(v.num) + 'mate= ' + str(v.mate.num))
                            #print(str(u.num) + 'mate= ' + str(u.mate.num))
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

class vertex(): 
#vertex will be parent class of reading activities and scheduled events classes
    def __init__(self, num):
        self.num=num 
        #mate and label are pointers to vertex
        self.label=None 
        self.mate=None       

    #def get_match(self):
        #return self.mate 

    def print_vertex(self):
        print(self.num, end=' ')

#main: test data to make sure class constructors and maching algorithm are working
#setV
v0= vertex(0)
v1= vertex(1)
v2= vertex(2)
v3= vertex(3)
v4= vertex(4)
#V=[]
#V
#V=set()
#V= {v0, v1, v2, v3, v4}

#setU
u5= vertex(5)
u6= vertex(6)
u7= vertex(7)
u8= vertex(8)
u9= vertex(9)
U= set()
U= {u5, u6, u7, u8, u9}

#Edge list
#E=[[5,6], [5], [5, 7], [7, 8, 9], [8, 9], [0, 1, 2], [0], [2, 3], [3, 4], [3, 4]]
E=[[u5,u6], [u5], [u5, u7], [u7, u8, u9], [u8, u9], [v0, v1, v2], [v0], [v2, v3], [v3, v4], [v3, v4]]

#make graph with and print to make sure class constructors work
graph1= graph(V, U, E)
#v0.print_vertex()
#graph1.print_queue()
#graph1.print_setV()

#class members not privagte can be changed or accessed outside of class
#v3.match=7
#u7.match=3
#u8.match=4
#v4.match=9
#print(v3.match)

print('before max_match')
graph1.print_matches()
graph1.max_match()
print('after max_match')
graph1.print_matches()
#graph1.print_set(graph1.unionVU)

for vertex in graph1.unionVU:
    print(vertex.num)
