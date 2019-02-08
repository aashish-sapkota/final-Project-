
file = open('lists.txt','r')
line = file.readlines()
l=[]
cproduct=[]# invoice banaunako laghi
cquantity=[]#invoice
cprice=[]#invoice banauna ko lai kam laghxa
totalko=[]#invoice
print("--------------Welcome to Sapkota Electronic store--------------  ")
print("S/N","\t\t","Products")
for i in range(len(line)):
    p = line[i].replace("\n","")
    q = p.split(',')
    l.append(q)
for j in range(len(l)):
    for k in range(len(l[j])):
        if k!=0:
            l[j][k]=int(l[j][k])#quantity ra price lai int ma change gareko
for a in range(len(l)):
    print(a+1,'\t\t',l[a][0],'\t\t\t')
print('---------------------------------------------------------------')
name = input('Enter Customer name: ')
ans = 'y'
while ans=='y':
    product = input('Enter product you want to buy: ')
    for y in range(len(l)):
        if product==l[y][0]:
            quantity = int(input('Enter the quantity: '))
            cquantity.append(quantity)
            quant = l[y][2] - quantity
            l[y][2]=quant
            cprice.append(l[y][1])
            quantprice=quantity*(l[y][1])
            totalko.append(quantprice)
            break
        
    cproduct.append(product)
    ans = input('do you want to buy any other product(y/n): ')
#print(l)
#print(cproduct)
#print(cquantity)
#print(cprice)
total=0
for pri in totalko:
    total=total+pri
#print(total)   
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]=str(l[i][j])
#print(l)
file = open('lists.txt','w')
for i in range(len(l)):
    z=(l[i][0]+','+l[i][1]+','+l[i][2]+'\n')
    file.writelines(z)
file.close()
print('------------------------------------------------------------------')
print("\n*****************************Inovice******************************")
print('Customers name: ',name)
print("------------------------------------------------------------------")
print('%10s'%"S/N",'%10s'%"Paricular",'%10s'%"Quantity",'%10s'%"Price",'%10s'%"\tAmount")
for i in range(0,len(cproduct)):
    print('%10d'%(i+1),'%10s'%cproduct[i],'%10d'%cquantity[i],'%10d'%cprice[i],'%10d'%totalko[i])
print ("\t\t\t\t\t\tTotal\t",total)
print('------------------------------------------------------------------')
file1=open('Invoice.txt','w')

In=('cutomername:'+name)
for i in range(len(cproduct)):
    Pr=(In+'\n'+'Product: '+str(cproduct[i])+'\n'+'Price: '+str(cprice[i])+'\n')
    file1.writelines(Pr)
file1.close()
for j in range(len(l)):  # again changing price & quantity into int data type 
    for k in range(len(l[j])):
            if k!=0:
                l[j][k]=int(l[j][k])
   





    

    
    




            
            
        
        
        
  
    
        
    
