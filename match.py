
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
