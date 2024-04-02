# generate USA-road-d.NAME.gr and USA-road-t.NAME.gr, d means cost and t means weight
import sys
from random import Random
import random
def gen_f(dirName:str,fileName:str,seed:int):
   randL=Random()
   randL.seed(seed)
   edges=[]
   n=-1
   m=-1
   with open(dirName+"/Graph.txt","r",encoding="UTF-8") as graph, open(dirName+'/'+fileName,"w",encoding="UTF-8") as res:
      for i in range(4):
         res.write("c fake map\n")
      while True:
         wordList=graph.readline().split()
         if not wordList:
            break
         if n==-1:
            n=int(wordList[0])
         else:
            edges.append(wordList)
      m=len(edges)
      res.write("p sp "+str(n)+" "+str(m*2)+"\n")
      res.write("c graph contains "+str(n)+" nodes and "+str(m*2)+" arcs\n")
      res.write("c\n")
      for wl in edges:
         l=str(randL.randint(1,1000))
         us=str(int(wl[0])+1)
         vs=str(int(wl[1])+1)
         res.write("a "+us+" "+vs+" "+l+'\n')
         res.write("a "+vs+" "+us+" "+l+'\n')
   return (n,m)

def gen_q(n:int,fileName:str,cnt:int):
   with open(fileName,"w",encoding="UTF-8") as qFile:
      for i in range(cnt):
         qFile.write(str(random.randint(0,n-1))+" "+str(random.randint(0,n-1))+" "+str(random.randint(n//10,n))+"\n")

def gen_graph(graphName:str):
   (n,m)=gen_f(graphName,"USA-road-t."+graphName+".gr",19260817)
   gen_f(graphName,"USA-road-d."+graphName+".gr",20021231)
   gen_q(n,graphName+"/random",200000)

if len(sys.argv)!=2:
    print("Error: too many or too few args")
else:
    gen_graph(sys.argv[1])
