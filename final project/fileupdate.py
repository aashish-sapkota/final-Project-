def fileupdate(l):
        for i in range(len(l)):# list is made str to write in txt file
            for j in range(len(l[i])):
                l[i][j]=str(l[i][j])
        file = open('lists.txt','w') #overwrite the stock file with decreased quantity.
        for i in range(len(l)):
            z=(l[i][0]+','+l[i][1]+','+l[i][2]+'\n')
            file.writelines(z)
        file.close()
        
