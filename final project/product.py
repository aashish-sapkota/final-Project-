def product(l,lproduct,cproduct,cquantity,cprice,totalko,name,total,discount,grandtotal):
    cproduct=[]# contains name of product that customer are willing to buy / used for making invoice
    cquantity=[]#quantity by customers / used for making invoice
    cprice=[]#price for each product that customer are willing to buy / used for making invoice
    totalko=[]# contains total of each product that customer are willing to buy / usedfor making invoice
    name = input('\nEnter Customer name: ').capitalize()
    ans = 'y'
    while ans=='y':
        product = input('Enter product you want to buy: ').capitalize()
        if product in lproduct:
            for y in range(len(l)):
                if product==l[y][0]:
                    s = False
                    while s==False:
                        try:  # if str is introduced (invalid)
                            quantity = int(input('Enter quantity: '))
                            quant = l[y][2] - quantity # to reduce the quantity of product after purchase
                            cquantity.append(quantity)
                            l[y][2]=quant
                            cprice.append(l[y][1])
                            quantprice=quantity*(l[y][1])
                            totalko.append(quantprice)
                            cproduct.append(product)
                            s = True
                        except:
                            print('invalid quantity.')
                        
        else:
            print('The product is not available.')

        ans = input('do you want to buy any other product(y/n): ')   
        if ans=='n':
            
            for pri in totalko:
                total=total+pri
            discount = (13/100)*total
            grandtotal = total-discount
    return l,lproduct,cproduct,cquantity,cprice,totalko,name,total,discount,grandtotal
        
    
    
