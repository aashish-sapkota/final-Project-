def Read(filename):
    file = open("lists.txt",'r')
    line = file.readlines()
    l=[]
    for i in range(len(line)):
        p = line[i].replace("\n","")
        q = p.split(',')
        l.append(q)
    for j in range(len(l)):  # changing price & quantity into int data type
        for k in range(len(l[j])):
            if k!=0:
                l[j][k]=int(l[j][k])
    return l
    
    

    
    
