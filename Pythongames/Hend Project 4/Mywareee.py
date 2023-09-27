from datetime import datetime
from tabulate import tabulate
#read files
customers=open("customers.csv",'r',encoding="utf8")
order_details=open("order_details.csv",'r',encoding="utf8")
orders=open("orders.csv",'r',encoding="utf8")
products=open("products.csv",'r',encoding="utf8")

#define a function to display the information for the user
def display_file(file,header):
    
    h = header.split(',')
    data = [h]
    for line in file:
        data.append(line.split(','))
    print(tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid'))

#define a function to insert a row in customer file
def insert_customer(filename):
    #CustomerNumber,CustomerName, Street, Number, Town, PostalCode, CreditLimit, CurrBalance
    cnumber=input("Enter customer number: ")
    name=input("Enter customer name: ")
    street=input("Enter street: ")
    number=input("Enter Number: ")
    town=input("Enter Town: ")
    postalcode=input("Enter Postal Code: ")
    creditLimit=input("Enter credit limit: ")
    currBalance=input("Enter CurrBalance: ")
    file=open(filename,"a")
    file.write(cnumber+","+name+","+street+","+number+","+town+","+postalcode+","+creditLimit+","+currBalance+"\n")
    file.close()
#define a function to insert a row in prodcuts file
def insert_products(filename):
    #ProductCode(*), Description, ListPrice, QantityOnPremises, ReorderLevel, ReorderQnty
    ProductCode=input("Enter ProductCode: ")
    Description=input("Enter Product Description: ")
    ListPrice=input("Enter ListPrice: ")
    QantityOnPremises=input("Enter QantityOnPremises: ")
    ReorderLevel=input("Enter ReorderLevel: ")
    ReorderQnty=input("Enter ReorderQnty: ")

    file=open(filename,"a")
    file.write(ProductCode+","+Description+","+ListPrice+","+QantityOnPremises+","+ReorderLevel+","+ReorderQnty+"\n")
    file.close()

#define a function to insert a row in order file
def insert_orders(filename):
    #OrderNumber(*), CustomerNumber(*), OrderDate, OrderTime
    OrderNumber=input("Enter Order Number: ")
    CustomerNumber=input("Enter Customer Number: ")
    OrderDate=input("Enter Order Date: ")
    OrderTime=input("Enter Order Time: ")

    file=open(filename,"a")
    file.write(OrderNumber+","+CustomerNumber+","+OrderDate+","+OrderTime+"\n")
    file.close()

#define a function to insert a row in order details file
def insert_orderDetails(filename):
    #OrderNumber(*), ProductCode, OrderQuantity, OrderPrice
    OrderNumber=input("Enter Order Number: ")
    ProductCode=input("Enter Product Code: ")
    OrderQuantity=input("Enter Order Quantity: ")
    OrderPrice=input("Enter Order Price: ")

    file=open(filename,"a")
    file.write(OrderNumber+","+ProductCode+","+OrderQuantity+","+OrderPrice+"\n")
    file.close()
def delete_data(fileName,uniqueIdentifier):
    fileData=[]
    found=False
    file=open(fileName,"r")
    for l in file:
        if uniqueIdentifier in l:
            found=True
        else:
            fileData.append(l)
    file.close()
    if found:
        file=open(fileName,"w")
        file.writelines(fileData)
        file.close()
        print("Deleted Successfully")
    else:
        print("Record Not found")
def modify_data(fileName,uniqueIdentifier):
    fileData=[]
    found=False
    file=open(fileName,"r")
    for l in file:
        if uniqueIdentifier in l:
            print(l)
            found=True
            if fileName=="customers.csv":
                name=input("Enter customer name: ")
                street=input("Enter street: ")
                number=input("Enter Number: ")
                town=input("Enter Town: ")
                postalcode=input("Enter Postal Code: ")
                creditLimit=input("Enter credit limit: ")
                currBalance=input("Enter CurrBalance: ")
                fileData.append(uniqueIdentifier+","+name+","+street+","+number+","+town+","+postalcode+","+creditLimit+","+currBalance+"\n")
            elif fileName=="products.csv":
                Description=input("Enter Product Description: ")
                ListPrice=input("Enter ListPrice: ")
                QantityOnPremises=input("Enter QantityOnPremises: ")
                ReorderLevel=input("Enter ReorderLevel: ")
                ReorderQnty=input("Enter ReorderQnty: ")
                fileData.append(uniqueIdentifier+","+Description+","+ListPrice+","+QantityOnPremises+","+ReorderLevel+","+ReorderQnty+"\n")
            elif fileName=="orders.csv":
                CustomerNumber=input("Enter Customer Number: ")
                OrderDate=input("Enter Order Date: ")
                OrderTime=input("Enter Order Time: ")
                fileData.append(uniqueIdentifier+","+CustomerNumber+","+OrderDate+","+OrderTime+"\n")
            elif fileName=="order_details.csv":
                ProductCode=input("Enter Product Code: ")
                OrderQuantity=input("Enter Order Quantity: ")
                OrderPrice=input("Enter Order Price: ")
                fileData.append(uniqueIdentifier+","+ProductCode+","+OrderQuantity+","+OrderPrice+"\n")
        else:
            fileData.append(l)
    file.close()
    if found:
        file=open(fileName,"w")
        file.writelines(fileData)
        file.close()
        print("Modified Successfully")
    else:
        print("Record Not found")


#define a function to list all pertinent information of a customer
def customer_info(customerNumber):
    found=False
    customerHeader="CustomerNumber,CustomerName,Street,Number,Town,PostalCode,CreditLimit,CurrBalance".split(",")
    orderHeader="OrderNumber,CustomerNumber,OrderDate,OrderTime".split(",")
    for l in customers:
        if customerNumber in l:
            found=True
            details=l.strip().split(",")
            for i in range(len(customerHeader)):
                print(customerHeader[i]+": "+details[i])
    if found:
        print("\nOrders by Customer\n")
        printStr = ''
        for i in range(len(orderHeader)):
            printStr += "{:<28}"
        print(printStr.format(*orderHeader))
        for l in orders:
            if customerNumber in l:
                details=l.strip().split(",")
                print(printStr.format(*details))
    else:
        print("Record Not Found")
    
def main():
    
    print("press 'd' to display file content")
    print("press 'i' to intert data in file")
    print("press 'de' to delete data from file")
    print("press 'm' to modify data in file")
    print("press 'cd' for all pertinent information of a customer")
    print("press 'cn' to display customer names")
    print("press 'pd' to display description and list price of all products")
    print("Press 'ct' to display the names of all customers who live in a specific Town")
    print("Press 'pc' to List the product code, description, order price and order quantity orders placed during specific month")
    print("press 'lc' to List the names of all customers who ordered a specific product with code  during a specific month")
    print("press 'bo' to value of the best order for a product with a specific name")
    print("press 'dv' to display date did we get our most valuable order ever")
    print("press 'lk' to list out the last k orders placed")
    print("press 'oc' to get product ordered in a specific month and total customers")
    print("press 'no' to list the customers who have not ordered in specific year")
    print("press 'mo' to customer who has ordered more than m times in a day")
    valid_list=['d','i','de','m','cd','cn','pd','ct','pc','lc','bo','dv','lk','oc','no','mo']
    choice=input().lower()
    while(choice not in valid_list):
        print('invalid input, please enter a valid input')
        print('-------------------------------------------')
        print("press 'd' to display file content")
        print("press 'i' to insert data in file")
        print("press 'de' to delete data from file")
        print("press 'm' to modify data in file")
        print("press 'cd' for all pertinent information of a customer")
        print("press 'cn' to display customer names")
        print("press 'pd' to display description and list price of all products")
        print("Press 'ct' to display the names of all customers who live in a specific Town")
        print("Press 'pc' to List the product code, description, order price and order quantity orders placed during specific month")
        print("press 'lc' to List the names of all customers who ordered a specific product with code  during a specific month")
        print("press 'bo' to value of the best order for a product with a specific name")
        print("press 'dv' to display date did we get our most valuable order ever")
        print("press 'lk' to list out the last k orders placed")
        print("press 'oc' to get product ordered in a specific month and total customers")
        print("press 'no' to list the customers who have not ordered in specific year")
        print("press 'mo' to customer who has ordered more than m times in a day")
        choice=input().lower()
    
    if choice=="d":
        while(True):
            print("press c for customers file")
            print("press o for orders file")
            print("press od for order_details file")
            print("press p for products file")
            choice2=input().lower()
            if choice2=="c":
                display_file(customers,"CustomerNumber,CustomerName,Street,Number,Town,PostalCode,CreditLimit,CurrBalance")
                break
            elif choice2=="o":
                display_file(orders,"OrderNumber,CustomerNumber,OrderDate,OrderTime")
                break
            elif choice2=="od":
                display_file(order_details,"OrderNumber,ProductCode,OrderQuantity,OrderPrice")
                break
            elif choice=="p":
                display_file(products,"ProductCode,Description,ListPrice,QantityOnPremises,ReorderLevel,ReorderQnty")
                break
            else:
                print("Wrong input! enter carefully")
    elif choice=="i":
        while(True):
            print("press c for customers file")
            print("press o for orders file")
            print("press od for order_details file")
            print("press p for products file")
            choice2=input().lower()
            if choice2=="c":
                insert_customer("customers.csv")
                break
            elif choice2=="o":
                insert_orders("orders.csv")
                break
            elif choice2=="od":
                insert_orderDetails("order_details.csv")
                break
            elif choice=="p":
                insert_products("products.csv")
                break
            else:
                print("Wrong input! enter carefully")
    elif choice=="de":
        while(True):
            print("press c for customers file")
            print("press o for orders file")
            print("press od for order_details file")
            print("press p for products file")
            choice2=input().lower()
            if choice2=="c":
                CustomerNumber=input("Enter Customer Number: ")
                delete_data("customers.csv",CustomerNumber)
                break
            elif choice2=="o":
                OrderNumber=input("Enter Order Number: ")
                delete_data("orders.csv",OrderNumber)
                break
            elif choice2=="od":
                OrderNumber=input("Enter Order Number: ")
                delete_data("order_details.csv",OrderNumber)
                break
            elif choice=="p":
                ProductCode=input("Enter Product Code: ")
                delete_data("products.csv",ProductCode)
                break
            else:
                print("Wrong input! enter carefully")
    elif choice=="m":
        while(True):
            print("press c for customers file")
            print("press o for orders file")
            print("press od for order_details file")
            print("press p for products file")
            choice2=input().lower()
            if choice2=="c":
                CustomerNumber=input("Enter Customer Number: ")
                modify_data("customers.csv",CustomerNumber)
                break
            elif choice2=="o":
                OrderNumber=input("Enter Order Number: ")
                modify_data("orders.csv",OrderNumber)
                break
            elif choice2=="od":
                OrderNumber=input("Enter Order Number: ")
                modify_data("order_details.csv",OrderNumber)
                break
            elif choice=="p":
                ProductCode=input("Enter Product Code: ")
                modify_data("products.csv",ProductCode)
                break
            else:
                print("Wrong input! enter carefully")
    elif choice=="cd":
        customerNumber=input("Enter Customer Number: ")
        customer_info(customerNumber)
    elif choice=="cn":
        print("Customer Names")
        for c in customers:
            customer=c.strip().split(",")
            print(customer[1])
    elif choice=="pd":
        print("Products description and Their List Price")
        print("{:<30}{:<20}".format("Product Description", "List Price"))
        for p in products:
            product=p.strip().split(",")
            
            print("   {:<27} $ {:<20}".format(product[1], product[2]))
    elif choice=="ct":
        townName=input("Enter Town Name: ").lower()
        found=False
        cust = []
        for c in customers:
            customer=c.strip().split(",")
            if customer[4].lower()==townName:
                cust.append(customer[1])
                found=True
        if found==False:
            print("No record found for this town")
        else:
            print("Customer Names")
            for c in cust:
                print(c)
    elif choice=="pc":
        while(True):
            month=input("Enter month (for example 08/21): ")
            m=month.split("/")
            if len(m)==2:
                orderList=[]
                displayData=[]
                for o in orders:
                    order=o.strip().split(",")
                    o2=order[2].split("-")
                    if o2[1]==m[0] and o2[2]==m[1]:
                        orderList.append(order[0])
                if len(orderList)==0:
                    print("No order placed in ",month)
                else:
                    orderDetails=[]
                    for ol in orderList:
                        for od in order_details:
                            order_detail=od.strip().split(",")
                            if order_detail[0]==ol:
                                
                                orderDetails.append([order_detail[1],order_detail[2],order_detail[3]])

                    for i in orderDetails:
                        for p in products:
                            product=p.strip().split(",")
                            if i[0]==product[0]:
                                displayData.append([product[0],product[1],i[2],i[1]])
                if len(displayData)==0:
                    print("No data found")
                else:
                    print("Orders Placed in this month.\n")
                    print("{:<20}{:<30}{:<25}{:<25}".format("Product code","Description","Order price","Order quantity"))
                    
                    for j in displayData:
                        print("{:<20}{:<30}{:<25}{:<25}".format(j[0], j[1], j[2], j[3]))
                break
            else:
                print("Wrong Input! Enter carefully")
    elif choice=="lc":
        product_code=input("Enter product code: ")
        while True:
            date=input("Enter order date(for example 01/21):")
            if "/" not in date or len(date) != 5:
                print("Wrong input, pelase enter carefully!")
            else:
                break
        m=date.split("/")
        found=False
        print("Customers who ordered " + str(product_code) + " on " + str(date))
        print()
        for p in order_details:
            pd=p.strip().split(",")
            if pd[1]==product_code:
                for o in orders:
                    od=o.strip().split(",")
                    
                    dt=o[2].split("-")
                    if m[1]==dt[0] and m[2]==dt[1]:
                        if pd[0]==od[0]:
                            for c in customers:
                                cd=c.strip().split(",")
                                if cd[0]==od[1]:
                                    found=True
                                    print(cd[1])         
        if found==False:
            print("No record found")
    elif choice=="bo":
        name=input("Enter product name: ")
        found=False
        found2=False
        best=""
        for p in products:
            if name.lower() in p.lower():
                pd=p.strip().split(",")
                product_code=pd[0]
                found=True
                price=0
                for o in order_details:
                    od=o.strip().split(",")
                    if product_code==od[1]:
                        best=od
                        found2=True
                        if price==0:
                            price=float(od[3])
                            
                        else:
                            if float(od[3])>price:
                                price=od[3]
                if found2:
                    print("Order Details\n")
                    print("{:<20}{:>15}".format("Order Number: ",best[0]))
                    print("{:<20}{:>15}".format("Product Code: ",best[1]))
                    print("{:<20}{:>15}".format("Order Quantity: ",best[2]))
                    print("{:<20}{:>15}".format("Order Price: ",best[3]))
                else:
                    print("No order found")
                break        
        if not found:
            print("No product found")
    elif choice=="dv":
        price=0
        ordernumber=""
        found=False
        found2=False
        for o in order_details:
            od=o.strip().split(",")
            if float(od[3])>price:
                price=float(od[3])
                ordernumber=od[0]
                found=True
        if found:
            for order in orders:
                ord=order.strip().split(",")
                if ord[0]==ordernumber:
                    print("On ",ord[3]," we get our most valuable order worth ",price)
                    found2=True
                    break
            if found2  ==False:
                print("order number ",ordernumber," with price ",price," is most valuable order but order detail is not available") 
        else:
            print("No record found")
    elif choice == "lk":
        while True:
            try:
                k = int(input("Input the how many recent orders to be displayed: "))
                if k < 1:
                    print("The input is not valid for the given order data")
                else:
                    orderI = []
                    for order in orders:
                        singleOrder = order.strip().split(',')
                        orderI.append(singleOrder)
                    orderI.sort(key=lambda date: datetime.strptime(date[2], "%d-%m-%y"))
                    recentOrders  = orderI[-k:]
                    print("Last " + str(k) + " orders")
                    print()
                    print("{:<20}{:<20}{:<20}{:<20}".format("Order ID", "Product ID", "Order Date", "Order Time"))
                    for order in recentOrders:
                        print("{:<20}{:<20}{:<20}{:<20}".format(order[0], order[1], order[2], order[3]))
            except:
                print("Wrong input, please try again")
                
    elif choice == "oc":
      
        while True:
            m = input('Enter the month and year (e.g 08/21): ')
            if "/" not in m or len(m) != 5:
                print("Wrong input, pelase enter carefully!")
            else:
                break
        m = m.split('/')
        productsDetails = {}
        ordersInMonth = []
        for order in orders:
            ord = order.strip().split(',')
            date = ord[2].split('-')
            if date[1] == m[0] and date[2] == m[1]:
                ordersInMonth.append(ord[0])
        productsInMonth = []
        for order in ordersInMonth:
            for orderDet in order_details:
                ordDet = orderDet.strip().split(',')
                if ordDet[0] == order:
                    if ordDet[1] in productsDetails:
                        if order in productsDetails[ordDet[1]]:
                            productsDetails[ordDet[1]][order][0] += 1
                        else:
                            productsDetails[ordDet[1]][order][0] = 1
                    else:
                        productsDetails[ordDet[1]] = {order: [1]}
                    productsInMonth.append(ordDet[1])
        print("Products in month " + m[0] + " of year " + m[1])
        print()
        print("{:<20}{:<25}".format("Product Code", "Total customers"))
        for prod in productsDetails:
            print("{:<20}{:<25}".format(prod, len(productsDetails[prod])))
            
    elif choice == "no":
        y = input('Enter the specific year: ')
        customersOrdered = []
        for order in orders:
            ord = order.strip().split(',')
            year = ord[2].split('-')[2]
            if year == y[-2:]:
                customersOrdered.append(ord[1])
        noOrderCustomers = []
        for customer in customers:
            cust = customer.strip().split(',')
            if cust[0] not in customersOrdered:
                noOrderCustomers.append(cust[1])
        print('Customers who have not ordered in Year ' + str(y))
        for customer in noOrderCustomers:
            print(customer)
    elif choice == "mo":
        while True:
            try:
                k = input("Please enter amount of orders in a day: ")
                k = int(k)
                ordersOnDay = {}
                ords = []
                for order in orders:
                    ords.append(order.strip().split(','))
                customersOrdered = [ord[1] for ord in ords]

                multipleOrderCust = [customer for customer in set(customersOrdered) if customersOrdered.count(customer) > k]

                for customer in multipleOrderCust:
                    for ord in ords:
                        if ord[1] == customer:
                            date = ord[2]
                            if customer in ordersOnDay:
                                if date in ordersOnDay[customer][0]:
                                    ordersOnDay[customer][0][date] += 1
                                else:
                                    ordersOnDay[customer][0][date] = 1
                            else:
                                ordersOnDay[customer] = [{date: 1}]
                customersOnCriteria = []
                for customer in ordersOnDay:
                    for date in ordersOnDay[customer][0]:
                        if ordersOnDay[customer][0][date] > k:
                            customersOnCriteria.append(customer)
                print("Customers' Names who have orderd more than " + str(k) + " times a day")
                for customer in customers:
                    cust = customer.strip().split(',')
                    if cust[0] in customersOnCriteria:
                        print(cust[1])
                break
            except:
                print("Error in the input, please enter correct input")
            




main()
