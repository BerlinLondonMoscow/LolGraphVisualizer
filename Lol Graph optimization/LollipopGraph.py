import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math
import numpy as np






Adjacency_Matrix_MSG = """
-------------------------------------------------------

Adjacency Matrix Format

v - Cycle Nodes
x - Path Nodes

[[v0,v1,...,vn,x0,x1,...,xm]
 [v0,v1,...,vn,x0,x1,...,xm]
 [v0,v1,...,vn,x0,x1,...,xm]
 [v0,v1,...,vn,x0,x1,...,xm]
 [v0,v1,...,vn,x0,x1,...,xm]
]

-------------------------------------------------------
"""








class node:
    def __init__(self,label,cords,neighbors = [], pebbleNum = 0):
        self.label = label;
        self.neighbors = [];
        self.pebbleNum = pebbleNum;
        self.cords = cords
    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)
    def add_pebble(self):
        self.pebbleNum +=1
    def assign_pebbleNum(self,number):
        self.pebbleNum = number;















class LollipopGraph:
    def __init__(self,Cycle_Length = 0,Path_Length = 0,Dist={}):
        self.Cycle_Length = Cycle_Length;
        self.Path_Length = Path_Length;
        self.Graph_Size = Cycle_Length + Path_Length

        #distribution
        D = {};
        print(Dist)
        for k in range(Cycle_Length):
            D["v"+str(k)] = 0;
        for k in range(Path_Length):
            D["x"+str(k)] = 0;
        
        
        for keys in D:
            if keys in Dist:
                D[keys] = Dist[keys]
        self.Dist = D
        
        #Creating Nodes

        Vertices = {}
        self.Vertices = Vertices;
        self.CycleX = []
        self.CycleY = []
        self.PathX = [1]
        self.PathY = [0]


        theta = 2*math.pi/self.Cycle_Length;
        #creating coords for cycle
        for i in range(self.Cycle_Length):
            #creating cycle nodes
            Vertices["v"+str(i)] = node("v"+str(i),[math.cos(i*theta),math.sin(i*theta)])

           
            self.CycleX.append(math.cos(i*theta))
            self.CycleY.append(math.sin(i*theta))
        
        #creating coords for path
        for i in range(self.Path_Length):
            
            #creating path nodes
            Vertices["x"+str(i)] = node("x"+str(i),[i+2,0])

           

            
            self.PathX.append(i+2)
            self.PathY.append(0)
        self.CycleX.append(1)
        self.CycleY.append(0)




        #recording distribution to vertices
            #cycle nodes
        
        for k in range(self.Cycle_Length):
             vertex = Vertices["v"+str(k)]
             vertex.assign_pebbleNum(self.Dist[vertex.label])

             #path nodes
        for k in range(self.Path_Length):
             vertex = Vertices["x"+str(k)]
             vertex.assign_pebbleNum(self.Dist[vertex.label])
        #recording adjacent vertices

            #cycle nodes
            # we need to check if the vertex is the final nth vertex so we can loop around or if we are starting at v1
        for i in range(self.Cycle_Length):
            if i == self.Cycle_Length-1:
                Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i)])
                Vertices["v"+str(i)].add_neighbor(Vertices["v0"])
                try:
                    Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i-1)])
                except:
                    print("cycle size is 1 or less")
            elif i == 0:
                 Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i)])
                 Vertices["v"+str(i)].add_neighbor(Vertices["v1"])
                 Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(Cycle_Length-1)])
                 try:
                    Vertices["v"+str(i)].add_neighbor(Vertices["x0"])
                 except:
                     print("Message[no path]")
            else:
                Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i)])
                Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i+1)])
                Vertices["v"+str(i)].add_neighbor(Vertices["v"+str(i-1)])

            

            #path nodes
        for i in range(Path_Length):
            if i == 0:
                    Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i)])
                    Vertices["x"+str(i)].add_neighbor(Vertices["v0"])
                    try:
                       Vertices["x"+str(i)].add_neighbor(Vertices["x1"])
                    except:
                        print("Message[no x1 vertex in path]")
            elif i == Path_Length-1:
                Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i-1)])
                Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i)])
            else:
                Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i)])
                Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i+1)])
                Vertices["x"+str(i)].add_neighbor(Vertices["x"+str(i-1)])
           




        
        
    
        matrix_list = np.zeros((self.Cycle_Length+self.Path_Length,self.Cycle_Length+self.Path_Length),dtype=int)

        for i in range(self.Cycle_Length):
            vertex = self.Vertices["v"+str(i)]
            for j in range(self.Cycle_Length):
                
                if self.Vertices["v"+str(j)] in vertex.neighbors:
                    matrix_list[i,j] = 1
                print(vertex.label,i,j,matrix_list[i,j])
            for j in range(self.Path_Length):
                
                if self.Vertices["x"+str(j)] in vertex.neighbors:
                    matrix_list[i,j+self.Cycle_Length] = 1   
                print(vertex.label,i,j+self.Cycle_Length,matrix_list[i,j+self.Cycle_Length])
        for i in range(self.Path_Length):
            vertex = self.Vertices["x"+str(i)]
            for j in range(self.Cycle_Length):
               
                if self.Vertices["v"+str(j)] in vertex.neighbors:
                    matrix_list[i+self.Cycle_Length,j] = 1
                print(vertex.label,i+self.Cycle_Length,j,matrix_list[i+self.Cycle_Length,j])
            for j in range(self.Path_Length):
                
                if self.Vertices["x"+str(j)] in vertex.neighbors:
                    matrix_list[i+self.Cycle_Length,j+self.Cycle_Length] = 1   
                print(vertex.label,i+self.Cycle_Length,j+self.Cycle_Length,matrix_list[i+self.Cycle_Length,j+self.Cycle_Length])
        self.adjacency_matrix = matrix_list
    def info(self):

        print(Adjacency_Matrix_MSG)
        print(self.adjacency_matrix,end="\n\n")

        print(f"{self.Graph_Size} nodes in graph",end="\n\n")
        #prints out the number of pebbles assigned to each vertex
        for key in self.Vertices:
            print(self.Vertices[key].label,"Pebbles: "+str(self.Vertices[key].pebbleNum))

    

    def updateDist(self,Dist):

        D = {};
        print(Dist)
        for k in range(self.Cycle_Length):
            D["v"+str(k)] = 0;
        for k in range(self.Path_Length):
            D["x"+str(k)] = 0;
        
        
        for keys in D:
            if keys in Dist:
                D[keys] = Dist[keys]
        self.Dist = D

         #recording distribution to vertices
            #cycle nodes
        
        for k in range(self.Cycle_Length):
             vertex = self.Vertices["v"+str(k)]
             vertex.assign_pebbleNum(self.Dist[vertex.label])

             #path nodes
        for k in range(self.Path_Length):
             vertex = self.Vertices["x"+str(k)]
             vertex.assign_pebbleNum(self.Dist[vertex.label])



    def drawGraph(self,show_labels = False,show_pebbling = False, CycleColor = "navy",PathColor = "brown"):

        
        #label the vertices 
        if show_pebbling:
            #show for cycle
            for k in range(self.Cycle_Length):
                vertex = self.Vertices["v"+str(k)]
                plt.text(vertex.cords[0]+0.2,vertex.cords[1]+0.02,str(vertex.label)+" ["+str(vertex.pebbleNum)+"]",size = 11)

            #show for path
            for k in range(self.Path_Length):
                vertex = self.Vertices["x"+str(k)]
                plt.text(vertex.cords[0]+0.2,vertex.cords[1]+0.02,str(vertex.label)+" ["+str(vertex.pebbleNum)+"]",size = 11)
        elif show_labels:
            #show for cycle
            for k in range(self.Cycle_Length):
                    vertex = self.Vertices["v"+str(k)]
                    plt.text(vertex.cords[0]+0.1,vertex.cords[1]+0.02,vertex.label,size = 11)

            #show for path
            for k in range(self.Path_Length):
                    vertex = self.Vertices["x"+str(k)]
                    plt.text(vertex.cords[0]+0.1,vertex.cords[1]+0.02,vertex.label,size = 11)
        
        plt.plot(self.PathX, self.PathY, marker = 'o',color = PathColor)

        

        #cycle plotting comes after to cover the (0,1) point of the path that is shared with the cycle. This is how we connect the two
        plt.plot(self.CycleX, self.CycleY, marker = 'o',color = CycleColor)


        #draw adjacency matrix
        plt.text(self.Path_Length,0.3,self.adjacency_matrix,color = "black",size = 11)

        plt.title("Lollipop Graph: "+"C_"+str(self.Cycle_Length)+" P_"+str(self.Path_Length))
        plt.show()
