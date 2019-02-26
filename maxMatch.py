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
            self.print_queue()
            self.print_debug('start of while')
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
                        #bug in while loop
                        while(v.label is not None):
                            #DEBUG
                            #self.print_debug('before')
                            u=v.label
                            if((u.mate == v) and (v.mate== u)):
                                v.mate=None
                                u.mate=None
                            v=u.label
                            v.mate=u
                            u.mate=v
                            #DEBUG
                            #self.print_debug('after')
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
V=list()
V= [v0, v1, v2, v3, v4]

#setU
u5= vertex(5)
u6= vertex(6)
u7= vertex(7)
u8= vertex(8)
u9= vertex(9)
U= list()
U= [u5, u6, u7, u8, u9]

U= [u5, u6, u7, u8]

# ------------------------------# 
#Edge list
# ------------------------------# 

#full endge list
E= {0:[u5,u6], 1:[u5], 2:[u5, u7], 3:[u7, u8, u9], 4:[u8, u9], 5:[v0, v1, v2], 6:[v0], 7:[v2, v3], 8:[v3, v4], 9:[v3, v4] }

#test with one less vertex.  U - u9
E= {0:[u5,u6], 1:[u5], 2:[u5, u7], 3:[u7, u8], 4:[u8], 5:[v0, v1, v2], 6:[v0], 7:[v2, v3], 8:[v3, v4]}

#class members not privagte can be changed or accessed outside of class
#v3.mate=u7
#u7.mate=v3
#v4.mate=u9
#u9.mate=v4
#v0.mate=u6
#u6.mate=v0


#make graph with and print to make sure class constructors work
graph1= graph(V, U, E)
#graph1.print_queue()
#graph1.print_setV()

print('before max_match')
graph1.print_matches()
graph1.max_match()
print('after max_match')
graph1.print_matches()
#graph1.print_set(graph1.unionVU)
