qun= []
Total = 0
total_amount = []
Tlist= []

print(" ")
print('\t\U0001F64F1WELCOME TO CASTLE BLACK CAFE\t\n')

food = {1:10,2:20,3:30,4:50,5:70,6:100,7:150,8:200,9:220,10:250,11:40,12:50,13:60,14:50,15:60,16:100,17:200,18:200,19:300,20:200}
food_name = {1:'Tea',2:'Coffee',3:'Cold coffee',4:'Soda',5:'juice',6:'Sandwich',7:'Pizza',8:'Grilled',9:'Rosted',10:'Burger',11:'Idali',12:'Dosa',13:'Pasta',14:'Upama',15:'Utthapa',16:'Vanila',17:'Cake',18:'Ice-cream',19:'Mango Cake',20:'Apple Cake'}

drink_print = """
        Drinks                  Price (Rs)

        1 . Tea             -   10
        2 . Coffee          -   20
        3 . Cold coffee     -   30
        4 . Soda            -   50
        5 . Juice           -   70
"""

wsnaks_print = """
        Western Snaks               Price(Rs)

        6 . sandwich            -   100
        7 . pizza               -   150
        8 . Grilled             -   200
        9 . Rosted              -   220
       10 . Burgur              -   250
"""

isnaks_print = """
        Indian Snaks               Price(Rs)

        11 . Idali              -   40
        12 . Dosa               -   50
        13 . Pasta              -   60
        14 . Upama              -   50
        15 . Uttapa             -   60
"""

Desert_print = """

        Deserts                  Price(Rs)

        16 . Vanila             -  40
        17 . Cake               -  50
        18 . Ice-cream          -  60
        19 . Mango-Cake         -  50
        20 . Apple-Cake         -  60
"""
flag = 'y'
name = input('Enter Your Name- ')
while flag.lower() == 'y':
    #name = input('Enter Your Name- ')
    print(f"\n Hello {name} , WELCOME TO OUR CAFE CASTLE BLACK\n ")
    print("What do you want - \n A.Drinks \n B.Indian Snaks \n C.Western snaks\n D.Dessert\n")
    que1 = input('Enter your Choice- ')

    if flag=='y':
        if que1.lower() == 'a':
            print(drink_print)
            drink1=int(input("Enter Your Order - "))
            Tlist.append(drink1)
            qdrink1=int(input('Enter the qunatity - '))
            qun.append(qdrink1)

        elif que1.lower() == 'b':
            print(isnaks_print)
            drink1=int(input("Enter Your Order - "))
            Tlist.append(drink1)
            qdrink1=int(input('Enter the qunatity - '))
            qun.append(qdrink1)

        elif que1.lower()=='c':
            print(wsnaks_print)
            drink1=int(input("Enter Your Order - "))
            Tlist.append(drink1)
            qdrink1=int(input('Enter the qunatity - '))
            qun.append(qdrink1)

        elif que1.lower()=='d':
            print(Desert_print)
            drink1=int(input("Enter Your Order - "))
            Tlist.append(drink1)
            qdrink1=int(input('Enter the qunatity - '))
            qun.append(qdrink1)
        else:
            print('Invild input')

        flag = input('Do You Want Something Else Y/N - ')

        if flag.lower() != 'y':


            
           
            
      







                import datetime  
                dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
                    datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
                    datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
                invoice = str(dt)  # unique invoice
                t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
                    datetime.datetime.now().day)  # date
                d = str(t)  # date
                u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
                    datetime.datetime.now().second)  # time
                e = str(u)  # time

                # d = date and e = time


                #invoice
                file = open(invoice + " (" + name + ").txt", "w")  
                file.write("=============================================================")
                file.write("\nCASTLE BLACK CAFE\t\t\t\tINVOICE")
                file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
                file.write("\nName of Customer: " + str(name) + "")
                file.write("\n=============================================================")
                file.write("\nFood Name\t\tQUANTITY\t\tFood PRICE\t\t\tTOTAL")
                file.write("\n-------------------------------------------------------------\n")
                for i in range(len(Tlist)):
                    Total =food[Tlist[i]]*qun[i]
                    total_amount.append(Total)
                    food_names =food_name[Tlist[i]]
                    qunatitys = qun[i]
                    prize = food[Tlist[i]]
                    Totals = Total
                    #s = "{:^12}{:^12}{:^12}{:^12}".format(food_names,qunatitys,prize,Totals)
                    #file.write(
                    #str("\n" + str(food_name[Tlist[i]]) + "\t\t\t" + str(qun[i]) + "\t\t\t\t " + str(food[Tlist[i]]) + "\t\t\t\t " + str(Total)))
                    file.write(str("\n{:^12}\t{:^12}\t{:^12}\t{:^12}".format(food_names,qunatitys,prize,Totals)))
                
                
                
                Tamount = sum(total_amount)
                
                

                
               
                file.write("\n-------------------------------------------------------------\n")
                file.write("\n\t\t\t Your payable amount is : " + str(Tamount))
                file.write("\n-------------------------------------------------------------\n")
                file.write("\n\n\tThank You " + name + " for your Food Shoping.\n\t\tSee you again!")
                file.write("\n=============================================================")
                file.close()





        


            

                


    
        








    


    

        
