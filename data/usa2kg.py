import sys
def usa_2_kg(dir_name:str):
    with open(dir_name+"/USA-road-t."+dir_name+".gr","r") as distFile , open(dir_name+"/USA-road-d."+dir_name+".gr","r") as costFile, open(dir_name+"/KG.txt","w") as kgFile:
        for i in range(7):
            distFile.readline()
        for i in range(4):
            costFile.readline()
        words=costFile.readline().split()
        print(words)
        n=int(words[2])
        m=int(words[3])
        for i in range(2):
            costFile.readline()
        kgFile.write("{}\n".format(n))
        for i in range(m):
            de=distFile.readline().split()
            ce=costFile.readline().split()
            u=int(de[1])
            v=int(de[2])
            if u<v:
                kgFile.write("{} {} {} {}\n".format(u,v,de[3],ce[3]))

if len(sys.argv)!=2:
    print("Error: too many or too few args")
else:
    usa_2_kg(sys.argv[1])