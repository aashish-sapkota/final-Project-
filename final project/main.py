import read
import Invoicefile
import fileupdate
import product
lproduct=[]
name=""
cproduct=[]# contains name of product that customer are willing to buy / used for making invoice
cquantity=[]#quantity by customers / used for making invoice
cprice=[]#price for each product that customer are willing to buy / used for making invoice
totalko=[]# contains total of each product that customer are willing to buy / usedfor making invoice
total=0
discount=0
grandtotal=0

print("--------------Welcome to Sapkota Electronic store--------------  ")
print("S/N","\t\t","Products")
print ("\t\t\t\t\t\t13%Discount\t")

l=read.Read('lists.txt')

for a in range(len(l)):
    print(a+1,'\t\t',l[a][0],'\t\t\t')
for i in range(len(l)):#to make condition for product not available 
    lproduct.append(l[i][0])
    
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

ask='n'
while ask=='n':
    l,lproduct,cproduct,cquantity,cprice,totalko,name,total,discount,grandtotal=product.product(l,lproduct,cproduct,cquantity,cprice,totalko,name,total,discount,grandtotal)   
    Invoicefile.invoice(name,cproduct,cquantity,cprice,totalko,total,discount,grandtotal)
    
    for i in range(len(cproduct)):# made empty for the use of new customer transaction.
            cproduct.remove(cproduct[i])
            cquantity.remove(cquantity[i])
            cprice.remove(cprice[i])
            totalko.remove(totalko[i])
            
    print('------------------------------------------------------------------')
    ans='n'
    fileupdate.fileupdate(l)
    for j in range(len(l)): # again changing price & quantity into int data type 
        for k in range(len(l[j])):
            if k!=0:
                l[j][k]=int(l[j][k])
    ask=input('do you want to exit(y/n): ')
    print('---------------------------------------------------------------')
print('Thank you for the visit')
print('---------------------------------------------------------------')
